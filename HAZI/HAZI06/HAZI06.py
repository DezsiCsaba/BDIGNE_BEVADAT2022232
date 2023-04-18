import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#from src.Node import Node
from Node import Node
#from DecisionTreeClassifier import DecisionTreeClassifier

from DecisionTreeClassifier import DecisionTreeClassifier
from NJCleaner import NJCleaner

#--------------------------------- DATA CLEANING
nj = NJCleaner('HAZI/HAZI06/2018_03.csv')
#nj = NJCleaner('HAZI/HAZI06/data/NJ_60k.csv')

nj.prep_df('HAZI/HAZI06/data/NJ.csv')
#nj.prep_df('HAZI/HAZI06/data/NJ_60k.csv')

#---------------------------------
col_name = ['sepal_lenght', 'sepal_width', 'petal_length', 'petal_width', 'type']
data = pd.read_csv('HAZI/HAZI06/data/NJ.csv',skiprows=1, header=None, names=col_name)
#data = pd.read_csv('HAZI/HAZI06/data/NJ_60k.csv',skiprows=1, header=None, names=col_name)

#---------------------------------
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2, random_state=41)


#---------------------------------
classifier = DecisionTreeClassifier(min_samples_split=2, max_depth=4)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))

"""
Megadott feladat alapján megírtam az NJCleaner-t. Ezek után kiszedtem a main-ből a szükséges .py fileokba a Node és DecisionTreeClassifier-t.
Ezeket beimportáltam a HAZI06.ipynb-be és teszteltem a működést.
Volt korábban egy kis félreírás fáradtsaág miatt, aeztért adott 0.93-makat.
A most átírt pedig egyszerűen nem tud 0.7853333333333333 felé menni...
Nehézségek:
    - Másképp kezeli a .ipynb-ben és .py-ban a file elérési utakat. Mire meglett h miért nem találja. És van egy pár 'path' és 3-szor indítottam meg a .py-t
    mire mindet átírtam. Bár ez inkább figyelmetlenség mint nehézség.
    - Kicsit katyvasz volt úfgy az egész feladat és ismerőstől segítéget kellett kérni h megértsem
Eredmények:
    i/    min_samples_split:  max_depth:  accuracy:
    1/            1               1       0.7773333333333333
    2/            3               4       0.7853333333333333
    3/            3               3       0.78325
    3/            2               4       0.7853333333333333
"""
