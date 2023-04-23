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
import random

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
