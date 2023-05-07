from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from skimage import io

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.ensemble import RandomForestClassifier
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from helpers import generate_data, predict_winner_from_random_data, base64_to_image, save_image_from_url, compare_faces, resize_image, compare_faces_aws, verify_jwt
import matplotlib.pyplot as plt
import base64
import cv2
import numpy as np
from skimage import io as sk_io
import face_recognition
import boto3
import os

# server start command: uvicorn main:app --reload
geolocator = Nominatim(user_agent="myGeocoder")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import random

np.random.seed(41)

# Import data from training_data.csv
data = pd.read_csv('training_data.csv')

# remove the scores column
data = data.drop(['score'], axis=1)

# Generate target variable (is_winner)
labels = data['is_winner'].to_numpy()

# Create a GroupShuffleSplit object
group_split = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

# Split the data into training and testing sets
train_idx, test_idx = next(group_split.split(data, groups=data['group_id']))
train_data = data.iloc[train_idx]
test_data = data.iloc[test_idx]

# Separate features and target variable for training and testing sets
X_train = train_data.drop(['group_id', 'candidate_id', 'is_winner'], axis=1)
y_train = train_data['is_winner']
X_test = test_data.drop(['group_id', 'candidate_id', 'is_winner'], axis=1)
y_test = test_data['is_winner']

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Load model if it exists, train a new one otherwise
if os.path.exists('model.pkl'):
    print("Loading model...")
    model = joblib.load('model.pkl')
else:
    print("Training model...")
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train_scaled, y_train)
    joblib.dump(model, 'model.pkl') 

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Get the feature importances
feature_importances = model.feature_importances_

# Print the feature importances
feature_names = X_train.columns
for name, importance in zip(feature_names, feature_importances):
    print(f"{name}: {importance}")

# Evaluate the model
print("Accuracy: {:.2f}".format(model.score(X_test_scaled, y_test)))

#predict_winner_from_random_data(100, 10, X_train, model)
 

@app.post("/calculate_winner")
async def calculate_winner(data: dict):
    winner = {}
    bids = data["data"]
    jwt_token = data["jwt"]
    #print(jwt_token)

    decoded_jwt = verify_jwt(jwt_token)
    if decoded_jwt is None:
        print("Invalid JWT, exiting...")
    else:
        print("JWT is valid, continuing...")

    

    for bid in bids:
        bidder_location = geolocator.geocode(f"{bid['city']}")
        seller_location = geolocator.geocode(f"{bid['poster_city']}")


        if bidder_location is None or seller_location is None:
            distance = 500
        else: 
            distance = geodesic((bidder_location.latitude, bidder_location.longitude), (seller_location.latitude, seller_location.longitude)).km

        print(f"Distance between {bid['city']} and {bid['poster_city']} is {distance:.2f} km")
        bid["distance"] = round(distance, 1)

        bid["job_duration"] = bid["bid_completion_time"]
        # remove city, country, poster_city, poster_country
        bid.pop("city", None)
        bid.pop("country", None)
        bid.pop("poster_city", None)
        bid.pop("poster_country", None)
        bid.pop("bid_completion_time", None)
    
    bids_df = pd.DataFrame(bids)
    # Add group_id and rename bidder_id to candidate_id
    bids_df['group_id'] = 0
    bids_df.rename(columns={'bidder_id': 'candidate_id'}, inplace=True)
    # Reorder the columns to match the order of the input features of the model
    bids_df = bids_df[['group_id', 'candidate_id', 'bid_amount', 'completion_date_diff', 'buyer_rating', 'past_jobs', 'account_age', 'distance', 'job_duration']]

    # Standardize the new data
    scaler = StandardScaler()
    X = scaler.fit_transform(bids_df.drop(['group_id', 'candidate_id'], axis=1))

    # print the features
    print(bids_df.drop(['group_id', 'candidate_id'], axis=1))

    # Make predictions on the new data
    y_pred = model.predict_proba(X)

    # Add the winning probabilities to the DataFrame
    winner_index = np.argmax(y_pred[:, 1])
    
    # get the winner's bidder_id
    winner["bidder_id"] = bids[winner_index]["bidder_id"]

    # add the winning probabilities to the DataFrame, multiplied by 100 to get the percentage
    bids_df["winning_probability"] = y_pred[:, 1] * 100


    # save bids_df to csv
    bids_df.to_csv("bids.csv", index=False)
    print("The predicted winner's id is: ", winner["bidder_id"])

    

    return {"winner": winner}


@app.post("/confirm_identity")
async def confirm_identity(data: dict):
    # Extract the base64 encoded image data from the data
    selfie_data = data["selfieDataUrl"]
    document_data = data["photoURL"]
    

    if ',' in selfie_data:
        selfie_data = selfie_data.split(",")[1]

    # Convert the base64 encoded strings to PIL Image objects

    img_data = base64.b64decode(str(selfie_data))
    with open("image.png", "wb") as image:
        image.write(img_data)

    # Save the document image from the URL
    document_image_file_name = "document_image.jpg"
    save_image_from_url(document_data, document_image_file_name)

    # Display the selfie and document images using matplotlib
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    axs[0].imshow(sk_io.imread("image.png"))
    axs[0].set_title("Selfie Image")
    axs[0].axis("off")

    axs[1].imshow(sk_io.imread(document_image_file_name))
    axs[1].set_title("Document Image")
    axs[1].axis("off")

    plt.show()
    """


    selfie_image = cv2.imread("image.png")
    document_image = cv2.imread("document_image.jpg")

    # Resize the images to 600x600
    selfie_image = resize_image(selfie_image, 600)
    document_image = resize_image(document_image, 600)
    selfie_image = cv2.flip(selfie_image, 1)


    cv2.imshow('Selfie Image', selfie_image)
    cv2.imshow('Document Image', document_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # First way of comparing faces
    # match_percentage = compare_faces(selfie_image, document_image)


    # get the face encodings for each face
    selfie_face_encodings = face_recognition.face_encodings(selfie_image)
    document_face_encodings = face_recognition.face_encodings(document_image)

    # check if either image couldn't be processed
    if len(selfie_face_encodings) == 0 or len(document_face_encodings) == 0:
        print("No faces found in one or both images.")
        variable = {"matchPercentage": 0}
    else:
        # there might be multiple faces in an image, so take the first one
        selfie_face_encoding = selfie_face_encodings[0]
        document_face_encoding = document_face_encodings[0]

        # compare faces and get euclidean distance
        face_distances = face_recognition.face_distance([selfie_face_encoding], document_face_encoding)

        # define your threshold (tweak this based on your requirements)
        match_threshold = 1

        # calculate match percentage
        if face_distances[0] <= match_threshold:
            match_percentage = (1 - face_distances[0]) / match_threshold * 100
        else:
            match_percentage = 0

        print(f"Match Percentage: {match_percentage:.2f}%")
        variable = {"matchPercentage": match_percentage}

    similarity = compare_faces_aws("image.png", "document_image.jpg")

    return {"similarity": similarity}

