from LinearRegressionSkeleton import LinearRegression
import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

Lreg = LinearRegression()

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

X = df['petal length (cm)'].values
y = df['petal width (cm)'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


Lreg.fit(X_train, y_train)
y_pred = Lreg.predict(X_test)
print(Lreg.evaluate(X_test, y_test))

# plt.scatter(Lreg.X_train, Lreg.y_train)
plt.scatter(X_test, y_test)
plt.plot([min(X_test), max(X_test)], [min(y_pred), max(y_pred)], color='red')  # predicted

plt.show()