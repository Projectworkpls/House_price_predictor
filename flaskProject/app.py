from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load the data from CSV file
data = pd.read_csv(r'C:\Users\LENOVO\Documents\DBS mini project\Housing - Copy.csv')

# Split the data into features (X) and target variable (y)
X = data.drop('price', axis=1)
y = data['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        # Convert input values to numeric format
        features = [float(data['Area']), float(data['Bedrooms']), float(data['Bathrooms']), float(data['Stories'])]
        prediction = model.predict([features])[0]  # Extracting the predicted price from the array
        return jsonify({'predicted_price': float(prediction)})  # Ensure the prediction is converted to a float
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
