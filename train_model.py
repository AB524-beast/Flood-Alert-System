# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load your historical data (make sure to replace 'historical_flood_data.csv' with your dataset)
data = pd.read_csv('historical_flood_data.csv')

# Assume the dataset contains these columns: 'location', 'weather_data', 'river_levels', 'environmental_data', 'flood_occurred'
X = data[['weather_data', 'river_levels', 'environmental_data']]
y = data['flood_occurred']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model using joblib for use in the Flask API
joblib.dump(model, 'flood_prediction_model.pkl')

print("Model trained and saved as 'flood_prediction_model.pkl'")
