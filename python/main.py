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
from helpers import generate_data, predict_winner_from_random_data
import matplotlib.pyplot as plt
import itertools



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

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

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
#print(classification_report(y_test, y_pred))


predict_winner_from_random_data(100, 10, X_train, model)
 



@app.post("/calculate_winner")
async def calculate_winner(data: dict):
    winner = {}
    bids = data["data"]

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
    photoURL = data["photoURL"]

    print('confirm_identity')
    return {"variable": photoURL}