import pandas as pd

def extract_features(data):
    # Example: Feature extraction from merged data
    data['odds_diff'] = data['home_odds'] - data['away_odds']
    data['total_goals'] = data['home_goals'] + data['away_goals']

    # Select important features
    features = data[['odds_diff', 'total_goals']]

    return features
