from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from KNNClassifier import KNNClassifier
import pandas as pd
import numpy as np
import os

relativePath = './segundoTrabalho/dataset.csv'
data = pd.read_csv(os.path.abspath(relativePath))

# Dividir o conjunto de dados em recursos (X) e rótulos (y)
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values  


# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# knn = KNNClassifier(k=3)

# knn.fit(X_train, y_train)

# y_pred = knn.predict(X_test)

# accuracy = np.mean(y_pred == y_test)
# print("Accuracy:", accuracy)