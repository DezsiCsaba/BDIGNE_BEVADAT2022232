# %%
import numpy as np
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import seaborn as sns

# %% [markdown]
# - Mudliból kapott .csv file-t és feladatleírást felhasználva kell megvalósítani a felhasználni kívánt fv-eket
# - py -m pip install seaborn

# %%
#basic .csv import inti (x,y) tuple

def load_csv(cs_path : str):
    np.random.seed(42)
    dataset = np.genfromtxt(cs_path, delimiter=',')
    np.random.shuffle(dataset)
    x,y = dataset[:, :-1],dataset[:, -1]
    return x,y

x,y = load_csv("iris.csv")
x.shape,y.shape

# %%
# this is kinda shitty
#np.mean(x, axis=0), np.var(x, axis=0)

# %%
np.nanmean(x, axis=0), np.nanvar(y, axis=0)

# %%
x[np.isnan(x)] = 3.5

# %%
less_than_zero = np.where(x < 0.0)
higher_than_ten = np.where(x > 10.0)

print(less_than_zero)
print(higher_than_ten)

# %%
x[np.where(np.logical_or(x > 10.0, x < 0.0))]

# %%
#delete sorindexeket vár axis=0-ra
#ezek után tisztább lesz a data

y = np.delete(y, np.where(x <0.0)[0], axis=0)
y = np.delete(y, np.where(x>10.0)[0], axis=0)
x = np.delete(x, np.where(x <0.0)[0], axis=0)
x = np.delete(x, np.where(x>10.0)[0], axis=0)

# %% [markdown]
# 
# ## BELOW COMES THE KNN
# ### Train test split function:

# %%
def train_test_splitting(features: np.ndarray,
                        labels: np.ndarray,
                        test_split_ratio: float):
    
    #meghatározzuk, hogy hol szeretnénk ketté vágni
    #ebből fog adódni, hogy mekkora a train_size
    test_size = int(len(features) * test_split_ratio)

    train_size = len(features)-test_size
    assert len(features) == test_size + train_size, "Size mismatch!"

    x_train, y_train = features[:train_size, :], labels[:train_size]
    x_test, y_test = features[train_size:, :], labels[train_size:]

    return (x_train, y_train, x_test, y_test)

# %%
x_train, y_train, x_test, y_test = train_test_splitting(x, y, 0.2)

# %% [markdown]
# ### KNN logic implementation:

# %% [markdown]
# - euclidean
# - $\sqrt{\sum_{i=1}^{k}(x_i - y_i)^2}$

# %%
# kettő közti különbség négyzetének Sum-ja
def euclidean(points: np.ndarray, element_of_x: np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum((points - element_of_x)**2, axis=0))

# %%
def predict(x_train: np.ndarray,
            y_train: np.ndarray,
            x_test: np.ndarray,
            k:int):
    labels_pred = []
    for x_test_element in x_test:
        # Táv
        distances = euclidean(x_train, x_test_element)
        distances = np.array(sorted(zip(distances, y_train)))
        #Leggyakoribb value
        #dist móduszán
        labels_pred = mode(distances[:k, 1], keepdims =False).mode
        labels_pred.append(labels_pred)

    return np.array(labels_pred, dtype=np.int64)

# %%
def accuracy(y_test: np.ndarray, y_preds: np.ndarray)->float:
    true_positive= (y_test == y_preds).sum()
    return true_positive / len(y_test) *100

# %%
#accuracy(y_test, y_preds)


