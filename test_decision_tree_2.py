from sklearn.tree import DecisionTreeRegressor
import numpy as np

# axies
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([10, 20, 22, 23, 25])

# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)

regr_1.fit(X, y)
regr_2.fit(X, y)

y_pred_1 = regr_1.predict(X)
print("y pred 1: ", y_pred_1)
y_pred_2 = regr_2.predict(X)
print("y pred 2: ", y_pred_2)


