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
nj.prep_df('HAZI/HAZI06/data/NJC.csv')


#---------------------------------
col_name = ['sepal_lenght', 'sepal_width', 'petal_length', 'petal_width', 'type']
data = pd.read_csv('HAZI\HAZI06\data\Iris.csv',skiprows=1, header=None, names=col_name)


#---------------------------------
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2, random_state=41)


#---------------------------------
classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))

"""
Megadott feladat alapján megírtam az NJCleaner-t. Ezek után kiszedtem a main-ből a szükséges .py fileokba a Node és DecisionTreeClassifier-t.
Ezeket beimportáltam a HAZI06.ipynb-be és teszteltem a működést. 93,3-mas eredményt adott a futás után.
Nehézségek:
    - Másképp kezeli a .ipynb-ben és .py-ban a file elérési utakat. Mire meglett h miért nem találja. És van egy pár 'path' és 3-szor indítottam meg a .py-t
    mire mindet átírtam. Bár ez inkább figyelmetlenség mint nehézség.
    - Kicsit katyvasz volt úfgy az egész feladat és ismerőstől segítéget kellett kérni h megértsem
Eredmények:
Ezt a részt figyelmen kívül hagytam. Mai nap folyamán még pótlásra kerül. Csak idő lesz lefuttatni néhányszor és rögzíteni az erdedményeket.
"""
