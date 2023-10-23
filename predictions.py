# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load historical weather data (you would need a larger dataset)
data = pd.read_csv('historical_weather_data.csv')

# Feature engineering and preprocessing (simplified for demonstration)
data['Temperature_Difference'] = data['Max_Temperature'] - data['Min_Temperature']
data['Rain_Threshold'] = (data['Precipitation'] > 0.0).astype(int)

# Define features and target variable
features = ['Max_Temperature', 'Min_Temperature', 'Humidity', 'Wind_Speed', 'Rain_Threshold']
target = 'Next_Day_Rain'

X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a machine learning model (Random Forest classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions for the next day's weather
predicted_weather = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predicted_weather)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Save the trained model for future use
import joblib
joblib.dump(model, 'weather_prediction_model.pkl')
