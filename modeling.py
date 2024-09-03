from pycaret.classification import setup, compare_models, finalize_model
import pandas as pd

def train_model(features, labels):
    data = pd.concat([features, labels], axis=1)

    # Set up PyCaret for classification
    clf_setup = setup(data, target='match_outcome', silent=True, verbose=False)

    # Compare models and select the best
    best_model = compare_models()

    # Finalize the model
    finalized_model = finalize_model(best_model)

    return finalized_model
