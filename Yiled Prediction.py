

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
rainfall = np.array([300, 400, 250, 500, 350])
fertilizer = np.array([40, 50, 30, 60, 45])
yield_data = np.array([550, 655, 430, 770, 600])

# Combine rainfall and fertilizer into one dataset
X = np.column_stack((rainfall, fertilizer))
y = yield_data

# Fit regression model
model = LinearRegression()
model.fit(X, y)

print("Coefficient for rainfall:", model.coef_[0])
print("Coefficient for fertilizer:", model.coef_[1])
print("Intercept:", model.intercept_)

# Predict yield for new values
predicted = model.predict([[200, 40]])
print("Predicted yield:", predicted[0], "kg/ha")

