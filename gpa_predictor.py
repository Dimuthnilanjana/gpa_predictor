# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1es9TPR8re5G5vPLLg5KxySi2rLgF45cI
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

"""Load the dataset"""

data = pd.read_csv('gpa.csv')

# Step 2: Data Preprocessing
# Assuming that the columns 'Subject1' through 'Subject12' contain marks and 'Overall_GPA' is the target variable
features = data[['Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Subject6']]
target = data['Overall_GPA']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 4: Choose a Model
model = LinearRegression()

# Step 5: Train the Model
model.fit(X_train, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')
print(f'R-squared: {r2}')

# Step 7: Make Predictions
# Assuming 'new_data' contains the marks for the 6 selected subjects
mark1 = 75
mark2 = 82
mark3 = 90
mark4 = 88
mark5 = 79
mark6 = 95

new_data = pd.DataFrame({'Subject1': [mark1], 'Subject2': [mark2], 'Subject3': [mark3],
                         'Subject4': [mark4], 'Subject5': [mark5], 'Subject6': [mark6]})

predicted_gpa = model.predict(new_data)

print(f'Predicted Overall GPA: {predicted_gpa[0]}')