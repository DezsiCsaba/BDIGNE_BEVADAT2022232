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
Lreg.predict(X)


plt.scatter(Lreg.X_train, Lreg.y_train)
plt.scatter(Lreg.X_test, Lreg.y_test)
#plt.plot([min(Lreg.X_test), max(Lreg.X_test)], [min(Lreg.y_pred), max(Lreg.y_pred)], color='red') # predicted
plt.show()