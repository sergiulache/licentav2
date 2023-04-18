from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


# server start command: uvicorn main:app --reload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import random

num_samples = 1000

# Generate random data
bid_amounts = np.random.randint(50, 2000, size=num_samples)
completion_date_diffs = np.random.randint(-30, 30, size=num_samples)
buyer_ratings = np.random.uniform(0, 5, size=num_samples)
past_jobs = np.random.randint(0, 100, size=num_samples)
account_ages = np.random.randint(0, 365, size=num_samples)
job_durations = np.random.randint(1, 30, size=num_samples)
distances = np.random.randint(1, 1000, size=num_samples)

# Create a pandas DataFrame
data = pd.DataFrame({
    'bid_amount': bid_amounts,
    'completion_date_diff': completion_date_diffs,
    'buyer_rating': buyer_ratings,
    'past_jobs': past_jobs,
    'account_age': account_ages,
    'job_duration': job_durations,
    'distance': distances
})


# Generate target variable (e.g., whether a buyer wins or loses the auction)
# This can be randomly generated for now, but in a real use case, you'll need actual labels
labels = np.random.randint(0, 2, size=num_samples)

#Split the data into training and testing sets:
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the AI model. In this example, we use Logistic Regression, but you can try other models
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy}")

# Use the model to predict the winner
# Replace the values with your actual data from the Svelte app
new_data = pd.DataFrame({
    'bid_amount': [1000],
    'completion_date_diff': [10],
    'buyer_rating': [4.5],
    'past_jobs': [50],
    'account_age': [200],
    'job_duration': [14],
    'distance': [300]
})

# Standardize the new data
new_data_scaled = scaler.transform(new_data)

# Generate 5 candidates
num_candidates = 5

# Generate random data
bid_amounts = np.random.randint(50, 2000, size=num_candidates)
completion_date_diffs = np.random.randint(-30, 30, size=num_candidates)
buyer_ratings = np.random.uniform(0, 5, size=num_candidates)
past_jobs = np.random.randint(0, 100, size=num_candidates)
account_ages = np.random.randint(0, 365, size=num_candidates)
job_durations = np.random.randint(1, 30, size=num_candidates)
distances = np.random.randint(1, 1000, size=num_candidates)

# Create a pandas DataFrame
candidates_data = pd.DataFrame({
    'bid_amount': bid_amounts,
    'completion_date_diff': completion_date_diffs,
    'buyer_rating': buyer_ratings,
    'past_jobs': past_jobs,
    'account_age': account_ages,
    'job_duration': job_durations,
    'distance': distances
})

print(candidates_data)

# Make a prediction
prediction = model.predict(candidates_data)
print(f"Predicted winner: {prediction[0]}")


@app.post("/calculate_winner")
async def calculate_winner(data: dict):
    # Implement your algorithm here
    # set winner equal to data
    winner = {}
    winner["ane"] = data["data"].upper()
    winner["pula"] = "pula"

    return {"winner": winner}
