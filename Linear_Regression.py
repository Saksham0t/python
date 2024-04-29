import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = np.array([2.4, 4.6, 5.5, 4.2, 6.2])
model = LinearRegression()
model.fit(X, y)
X_pred = np.array([[0], [6]])
y_pred = model.predict(X_pred)
plt.scatter(X, y, label='Data Points')
plt.plot(X_pred, y_pred, color='purple', linewidth=2, label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression')
plt.show()

