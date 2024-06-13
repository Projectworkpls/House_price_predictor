import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score, mean_absolute_error
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

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)


# Example: Predict the price of a new house
print("Enter the values for the following features:")
new_house_features = []
for column in X.columns:
    value = float(input(f"{column}: "))
    new_house_features.append(value)
X_train_df = pd.DataFrame(X_train, columns=['Area', 'Bedrooms', 'Bathrooms', 'Stories'])
model.fit(X_train_df, y_train)


# Make prediction for the new house
predicted_price = model.predict([new_house_features])
print(f"Predicted price of the new house: ${predicted_price[0]:.2f}")
