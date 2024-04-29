import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

data = pd.read_csv('\\Users\\sondh\\Downloads\\archive.csv')
print(data.head())
print(data.info())

X = data.drop(['rad', 'tax'], axis=1)
y = data['tax']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)

k_range = list(range(1, 50))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

plt.plot(k_range, scores)
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Accuracy Score')
plt.title('KNN Score for Different Values of K')
plt.show()
