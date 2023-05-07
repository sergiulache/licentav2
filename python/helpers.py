import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from skimage import io
from PIL import Image
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import base64
import requests
import cv2
import io
from skimage import io as sk_io
import face_recognition
import boto3
import jwt

np.random.seed(41)


weights = {
    'bid_amount': -10,
    'completion_date_diff': -2,
    'buyer_rating': 5,
    'past_jobs': 3,
    'account_age': 0.1,
    'job_duration': -1,
    'distance': -0.1
}

def generate_data(n_groups, candidates_per_group):
    num_samples = n_groups * candidates_per_group

    # Generate random data
    bid_amounts = np.random.randint(1000, 2000, size=num_samples)
    completion_date_diffs = np.random.randint(-30, 30, size=num_samples)
    buyer_ratings = np.random.randint(0, 6, size=num_samples)
    past_jobs = np.random.randint(0, 100, size=num_samples)
    account_ages = np.random.randint(0, 365, size=num_samples)
    job_durations = np.random.randint(1, 30, size=num_samples)
    distances = np.random.randint(1, 1000, size=num_samples)

    # Create a MinMaxScaler
    scaler = MinMaxScaler()
    # Scale the features
    bid_amounts_scaled = scaler.fit_transform(bid_amounts.reshape(-1, 1)).flatten()
    completion_date_diffs_scaled = scaler.fit_transform(completion_date_diffs.reshape(-1, 1)).flatten()
    buyer_ratings_scaled = scaler.fit_transform(buyer_ratings.reshape(-1, 1)).flatten()
    past_jobs_scaled = scaler.fit_transform(past_jobs.reshape(-1, 1)).flatten()
    account_ages_scaled = scaler.fit_transform(account_ages.reshape(-1, 1)).flatten()
    job_durations_scaled = scaler.fit_transform(job_durations.reshape(-1, 1)).flatten()
    distances_scaled = scaler.fit_transform(distances.reshape(-1, 1)).flatten()

    # Apply weights to each feature
    weighted_bid_amounts = bid_amounts_scaled * weights['bid_amount']
    weighted_completion_date_diffs = completion_date_diffs_scaled * weights['completion_date_diff']
    weighted_buyer_ratings = buyer_ratings_scaled * weights['buyer_rating']
    weighted_past_jobs = past_jobs_scaled * weights['past_jobs']
    weighted_account_ages = account_ages_scaled * weights['account_age']
    weighted_job_durations = job_durations_scaled * weights['job_duration']
    weighted_distances = distances_scaled * weights['distance']

    # Calculate the scores based on the weighted features
    scores = (weighted_bid_amounts + weighted_completion_date_diffs + 
            weighted_buyer_ratings + weighted_past_jobs +
            weighted_account_ages + weighted_job_durations +
            weighted_distances)
    
    score_shift = np.abs(np.min(scores)) + 1
    scores += score_shift

    group_id = np.repeat(np.arange(n_groups), candidates_per_group)
    candidate_id = np.arange(num_samples)

    # Create a pandas DataFrame
    data = pd.DataFrame({
        'group_id': group_id,
        'candidate_id': candidate_id,
        'bid_amount': bid_amounts,
        'completion_date_diff': completion_date_diffs,
        'buyer_rating': buyer_ratings,
        'past_jobs': past_jobs,
        'account_age': account_ages,
        'job_duration': job_durations,
        'distance': distances,
        'score': scores
    })

    # Assign winners based on the highest score in each group
    data['is_winner'] = 0
    winners_idx = data.groupby('group_id')['score'].idxmax()
    data.loc[winners_idx, 'is_winner'] = 1

    return data


def predict_winner_from_random_data(n_groups, candidates_per_group, X_train, model):
    num_new_samples = n_groups * candidates_per_group

    # Generate random data
    new_data = generate_data(n_groups, candidates_per_group)
    # add a candidate to the new data in the last group with bid amount 1000, the rest random
    new_data.loc[new_data['group_id'] == new_data['group_id'].max(), 'bid_amount'] = 1000

    # Standardize the new data
    # Standardize the new data
    new_X = new_data[X_train.columns]
    scaler = StandardScaler()
    scaler.fit(X_train)
    new_X_scaled = scaler.transform(new_X)



    # Make predictions on the new data
    new_y_pred = model.predict_proba(new_X_scaled)

    # Add the winning probabilities to the DataFrame
    # Get the max probability for each group
    new_data['score_difference_scaled'] = ((new_data.groupby('group_id')['score'].transform(max) - new_data['score']) ** 2).round(2) * 10


    # Save new_data to csv
    new_data.to_csv('new_data.csv', index=False)

    # Find the winners for each group
    winners = new_data.loc[new_data.groupby('group_id')['score'].idxmax()]
    winners = winners[['group_id', 'candidate_id', 'score']]
    print("\n\nPrinting winners:\n\n")
    print(winners)


def base64_to_image(base64_data):
    imgdata = base64.b64decode(str(base64_data))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return opencv_img 

def save_image_from_url(url, file_name):
    response = requests.get(url)
    with open(file_name, "wb") as image:
        image.write(response.content)

def resize_image(image, max_size):
    height, width = image.shape[:2]
    aspect_ratio = float(height) / float(width)
    
    if height > width:
        new_height = max_size
        new_width = int(new_height / aspect_ratio)
    else:
        new_width = max_size
        new_height = int(new_width * aspect_ratio)

    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized_image


def compare_faces(face1, face2):
    face1_encodings = face_recognition.face_encodings(face1)
    face2_encodings = face_recognition.face_encodings(face2)

    rotations = [0, 90, 180, 270]

    if len(face1_encodings) == 0:
        for angle in rotations:
            face1_rotated = np.rot90(face1, k=angle // 90)
            face1_encodings = face_recognition.face_encodings(face1_rotated)
            if len(face1_encodings) > 0:
                break

    if len(face2_encodings) == 0:
        for angle in rotations:
            face2_rotated = np.rot90(face2, k=angle // 90)
            face2_encodings = face_recognition.face_encodings(face2_rotated)
            if len(face2_encodings) > 0:
                break

    if len(face1_encodings) == 0 or len(face2_encodings) == 0:
        return 0

    face1_encoding = face1_encodings[0]
    face2_encoding = face2_encodings[0]

    match_result = face_recognition.compare_faces([face1_encoding], face2_encoding, tolerance=0.5)
    face_distances = face_recognition.face_distance([face1_encoding], face2_encoding)
    confidence = (1 - face_distances[0]) * 100

    return confidence if match_result[0] else 0


def compare_faces_aws(sourceFile, targetFile):
    client = boto3.client('rekognition')
    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')
    response = client.compare_faces(SimilarityThreshold=90,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        similarity = faceMatch['Similarity']
        print(f'Similarity: {similarity} %')
        return similarity
    if not response['FaceMatches']:
        print('Face doesn\'t match')
        return 0
        
    imageSource.close()
    imageTarget.close()


import jwt

def verify_jwt(jwt_token):
    # Replace the following string with your Supabase JWT secret
    supabase_jwt_secret = "KEImASZsg3WOGUG0vm6qcCbH+lDKNPPE5sGN2OQm3r3WKuWIQmf7Ns/2+XlqvjSWEVrqf0PQStkFWtkSCcBYuQ=="

    try:
        decoded = jwt.decode(
            jwt_token,
            supabase_jwt_secret,
            algorithms=["HS256"],
            audience="authenticated"  # Update the audience value here
        )
        return decoded
    except Exception as e:
        print(f"Error decoding JWT: {e}")
        return None


