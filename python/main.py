from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from geopy.geocoders import Nominatim
from geopy.distance import geodesic



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

def generate_data(n_groups, candidates_per_group, weights):
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

# Set the weights for each feature based on their priorities
"""
weights = {
    'bid_amount': -1,
    'completion_date_diff': -1,
    'buyer_rating': 1,
    'past_jobs': 1,
    'account_age': 0,
    'job_duration': -1,
    'distance': 0
}
"""

weights = {
    'bid_amount': -7,
    'completion_date_diff': -2,
    'buyer_rating': 4,
    'past_jobs': 2,
    'account_age': 0.1,
    'job_duration': -1,
    'distance': 0.1
}


n_groups = 1000
candidates_per_group = 10
num_samples = n_groups * candidates_per_group

# Generate the dataset
# data = generate_data(n_groups, candidates_per_group, weights)
# data.to_csv('fresh_data_1k.csv', index=False)
#
#
#

# Import data from training_data.csv

# Read the training_data.csv file
data = pd.read_csv('training_data.csv')

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

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

"""
# Get the feature importances
feature_importances = model.feature_importances_

# Print the feature importances
feature_names = X_train.columns
for name, importance in zip(feature_names, feature_importances):
    print(f"{name}: {importance}")

# Evaluate the model
print("Accuracy: {:.2f}".format(model.score(X_test_scaled, y_test)))
#print(classification_report(y_test, y_pred))
"""

# Use the model to predict the winner
# Generate new data for prediction
n_new_groups = 100
candidates_per_group = 10
num_new_samples = n_new_groups * candidates_per_group

# Generate random data
new_data = generate_data(n_new_groups, candidates_per_group, weights)
# add a candidate to the new data in the last group with bid amount 1000, the rest random
new_data.loc[new_data['group_id'] == new_data['group_id'].max(), 'bid_amount'] = 1000

# Standardize the new data
# Standardize the new data
new_X = new_data[X_train.columns]
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


@app.post("/calculate_winner")
async def calculate_winner(data: dict):
    # Implement your algorithm here
    # set winner equal to data
    winner = {}
    #winner["test1"] = data["data"].upper()
    winner["test2"] = "test2"

    bids = data["data"]

    for bid in bids:
        bidder_location = geolocator.geocode(f"{bid['city']}, {bid['country']}")
        seller_location = geolocator.geocode(f"{bid['poster_city']}, {bid['poster_country']}")

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
    
    print(bids)

    return {"winner": winner}
