# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as skl
from typing import Tuple

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error

# %%
'''
Készíts egy függvényt, betölti majd vissza adja az iris adathalmazt.


Egy példa a kimenetre: iris
return type: sklearn.utils.Bunch
függvény neve: load_iris_data
'''

# %%
#1
def load_iris_data() -> skl.utils.Bunch:
    return load_iris()

#irisData = load_iris_data()
#print(irisData)

# %%
'''
Készíts egy függvényt, ami a betölti az virágokhoz tartozó levél méretket egy dataframebe, majd az első 5 sort visszaadja.
Minden oszlop tartalmazza, hogy az milyen mérethez tartozik.

Egy példa a bemenetre: iris
Egy példa a kimenetre: iris_df
return type: pandas.core.frame.DataFrame
függvény neve: check_data
'''

# %%
#2
def check_data(iris) -> pd.core.frame.DataFrame:
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names).head(5)
    return iris_df

#check_data(irisData)

# %%
''' 
Készíts egy függvényt ami előkészíti az adatokat egy lineaáris regressziós model feltanításához.
Featurejeink legyenek a levél méretek kivéve a "sepal length (cm)", ez legyen a targetünk.

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: linear_train_data
'''

# %%
#3
def linear_train_data(iris) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    X = df[['sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].values
    y = df['sepal length (cm)'].values
    return X, y

#linear_train_data(irisData)

# %%
''' 
Készíts egy függvényt ami előkészíti az adatokat egy logisztikus regressziós model feltanításához.
Featurejeink legyenek a levél méretek, targetünk pedig a 0, 1-es virág osztályok.
Fontos csak azokkal az adatokkal tanítsunk amihez tartozik adott target. 

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: logistic_train_data
'''

# %%
#4
def logistic_train_data(iris) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    X = df.loc[np.where(iris.target < 2)].values
    y = iris.target[np.where(iris.target < 2)]
    return X,y

#X,y = logistic_train_data(irisData)

# %%
'''
Készíts egy függvényt ami feldarabolja az adatainkat train és test részre. Az adatok 20%-át használjuk fel a teszteléshez.
Tegyük determenisztikussá a darabolást, ennek értéke legyen 42.

Egy példa a bemenetre: X, y
Egy példa a kimenetre: X_train, X_test, y_train, y_test
return type: (numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray)
függvény neve: split_data
'''

# %%
#5
def split_data(X, y) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    split = train_test_split(X, y, test_size=0.2, random_state=42)
    return split

#X_train, X_test, y_train, y_test = split_data(X,y)

# %%
'''
Készíts egy függvényt ami feltanít egy lineaáris regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LinearRegression
függvény neve: train_linear_regression
'''

# %%
#6
def train_linear_regression(X_train, y_train) -> skl.linear_model._base.LinearRegression:
    model = LinearRegression().fit(X_train, y_train)
    return model

#lin_model = train_linear_regression(X_train, y_train)

# %%
'''
Készíts egy függvényt ami feltanít egy logisztikus regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LogisticRegression
függvény neve: train_logistic_regression
'''

# %%
#7
def train_logistic_regression(X_train, y_train) -> skl.linear_model._logistic.LogisticRegression:
    model = LogisticRegression(solver='liblinear', random_state=42).fit(X_train, y_train)
    return model

#log_model = train_logistic_regression(X_train, y_train)

# %%
''' 
Készíts egy függvényt, ami a feltanított modellel predikciót tud végre hajtani.

Egy példa a bemenetre: model, X_test
Egy példa a kimenetre: y_pred
return type: numpy.ndarray
függvény neve: predict
'''

# %%
#8
def predict(model, X_test) -> np.ndarray:
    y_pred =  model.predict(X_test)
    return y_pred

#y_pred_lin = predict(lin_model, X_test)
#print(predict(lin_model, X_test))

#y_pred_log = predict(log_model, X_test)
#print(predict(log_model, X_test))

# %%
'''
Készíts egy függvényt, ami vizualizálni tudja a label és a predikciók közötti eltérést.
Használj scatter plotot a diagram elkészítéséhez.

Diagram címe legyen: 'Actual vs Predicted Target Values'
Az x tengely címe legyen: 'Actual'
Az y tengely címe legyen: 'Predicted'

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: scatter plot
return type: matplotlib.figure.Figure
függvény neve: plot_actual_vs_predicted
'''

# %%
#9
def plot_actual_vs_predicted(y_test, y_pred) -> plt.Figure:
    scatter_plot, ax = plt.subplots()
    
    ax.scatter(y_test, y_pred)

    ax.set_title("Actual vs Predicted Target Values")
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    
    return scatter_plot


#plot_actual_vs_predicted(y_test, y_pred_lin)

# %%
''' 
Készíts egy függvényt, ami a Négyzetes hiba (MSE) értékét számolja ki a predikciók és a valós értékek között.

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: mse
return type: float
függvény neve: evaluate_model
'''

# %%
#10
def evaluate_model(y_test, y_pred) -> float:
    mse = mean_squared_error(y_test, y_pred)
    return mse

#evaluate_model(y_test, y_pred_lin)


