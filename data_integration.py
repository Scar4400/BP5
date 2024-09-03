from data_fetcher import fetch_all_data
from data_preprocessing import preprocess_data
from feature_engineering import extract_features
from modeling import train_model
import asyncio

def integrate_data_and_train():
    # Fetch all data
    data = asyncio.run(fetch_all_data())

    # Preprocess the data
    merged_data = preprocess_data(*data)

    # Extract features
    features = extract_features(merged_data)

    # Mock target variable (e.g., match outcome)
    labels = merged_data['match_outcome']

    # Train the model
    model = train_model(features, labels)

    return model
