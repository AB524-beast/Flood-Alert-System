# app.py
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained Random Forest model
model = joblib.load('flood_prediction_model.pkl')

# Load historical data (In practice, this could come from a database or an external API)
data = pd.read_csv('historical_flood_data.csv')

@app.route('/')
def index():
    return "Welcome to the Flood Prediction API!"

# Endpoint to accept location and return flood prediction
@app.route('/predict', methods=['POST'])
def predict_flood():
    # Get the location from the request
    location = request.json.get('location')

    # Retrieve historical data for the provided location
    location_data = data[data['location'].str.lower() == location.lower()]

    if location_data.empty:
        return jsonify({'error': 'No data available for this location'}), 404

    # Extract features for the prediction
    X_input = location_data[['weather_data', 'river_levels', 'environmental_data']].values

    # Predict using the loaded Random Forest model
    prediction = model.predict(X_input)

    # Interpret the prediction
    flood_prediction = 'Flood likely to occur' if prediction[0] == 1 else 'No flood expected'

    # Return the prediction as JSON
    return jsonify({
        'location': location,
        'prediction': flood_prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
