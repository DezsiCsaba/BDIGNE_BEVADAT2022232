# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!

# %%
#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
#Paraméterei: mérete (tupel-ként), default mérete pedig legyen egy (2,2)
#Be: (2,2)
#Ki: [[0,0],[0,0]]
#create_array()

def create_array(size = (2,2)):
    out = np.zeros(size, dtype=int)
    return out

#create_array((5,5))

# %%
#Készíts egy függvényt ami a paraméterként kapott array-t főátlót feltölti egyesekkel
#Be: [[1,2],
#     [3,4]]
#Ki: [[1,2],
#     [3,1]]
#set_one()

#def set_one(array):   
#    array = np.fill_diagonal(array, val=1)
#    return array

#set_one(np.ndarray([[1, 2], [3, 4]]))

# %%
# Transzponáld a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()

def do_transpose(arr):
    out = arr
    out.transpose
    return out

#do_transpose(np.array([[1, 2], [3, 4]]))

# %%
# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, alapértelmezetten 
# Be: [0.1223, 0.1675], n = 2
# Ki: [0.12, 0.17]
# round_array()

def round_array(arr, n):
    out=np.around(arr, decimals=n)
    return out

#round_array(np.array([0.1223, 0.1675]), 2)

# %%
# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 0 - False-ra az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()
def bool_array(arr):
    out=np.ma.masked_values(arr,1).mask
    return out

#bool_array(np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]]))

# %%
# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()

# %%
# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()

def bool_array(arr):
    out=np.ma.masked_values(arr,0).mask
    return out

#bool_array(np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]]))


