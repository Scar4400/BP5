from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the saved model
with open("saved_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features from input
    features = [data['odds_diff'], data['total_goals']]

    # Make prediction
    prediction = model.predict([features])[0]

    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
