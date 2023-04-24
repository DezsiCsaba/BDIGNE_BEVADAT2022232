from LinearRegressionSkeleton import LinearRegression
import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import numpy as np

Lreg = LinearRegression()

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

X = df['petal length (cm)'].values
y = df['petal width (cm)'].values

Lreg.fit(X, y)
y_pred = Lreg.predict(Lreg.X_test)
print(Lreg.evaluate(Lreg.X_test, Lreg.y_test))

# plt.scatter(Lreg.X_train, Lreg.y_train)
plt.scatter(Lreg.X_test, Lreg.y_test)
plt.plot([min(Lreg.X_test), max(Lreg.X_test)], [min(y_pred), max(y_pred)], color='red')  # predicted

plt.show()