import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
X = np.array([[1.0], [2.0], [2.5], [3.0], [4.0], [5.0], [5.5], [6.0]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
model = LogisticRegression()
model.fit(X, y)
X_pred = np.linspace(0, 7).reshape(-1, 1)
y_pred = model.predict_proba(X_pred)[:, 1]
plt.scatter(X, y, label='Data Points')
plt.plot(X_pred, y_pred, color='purple', linewidth=2, label='Logistic Regression')
plt.xlabel('X')
plt.ylabel('Probability of Class 1')
plt.legend()
plt.title('Logistic Regression')
plt.show()
