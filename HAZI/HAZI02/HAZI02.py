# %%
import numpy as np

# %%
# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

def column_swap(arr):
    out = arr
    #out[:, [1,0]] = out[:, [0,1]]
    out = np.fliplr(out)
    return out

column_swap(np.array([[1,2],[3,4]]))

# %%
#Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

def compare_two_array(arr1, arr2):
    out = np.array((arr1[:]==arr2[:])).astype(int)
    return np.nonzero(out)[0]

#compare_two_array(np.array([7,8,9]), np.array([9,8,7]))

# %%
#Készíts egy olyan függvényt, ami vissza adja a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!

def get_array_shape(arr):
    out = ("sor: " + str(arr.shape[0]) + ", oszlop: " + str(arr.shape[1]) + ", melyseg: " + str(arr.ndim))    
    return out

#get_array_shape(np.array([[1,2,3], [4,5,6]]))
#get_array_shape(np.array([[[1,2],[3,4]]]))

# %%
# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges Y-okat egy numpy array-ből. 
#Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

def encode_Y(arr, num):
    out = np.zeros(shape=(num,len(arr)), dtype=int)
    #print(out)
    indicies = np.expand_dims(arr, 1)
    #print(indicies)
    np.put_along_axis(out, indicies, 1, axis=1)
    return out

encode_Y(np.array([1, 2, 0, 3], dtype=int), 4)

# %%
# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

def decode_Y(arr):
    return np.where(arr==1)[1]

decode_Y(np.array([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]))

# %%
# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t
#és adja vissza a legvalószínübb element a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. 
# Ki: 'szilva'
# eval_classification()

def eval_classification(lst, arr):
    return lst[np.where(arr==np.amax(arr))[0][0]]

#eval_classification(['alma', 'körte', 'szilva'], np.array([0.3, 0.2, 0.6]))


# %%
# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()

def repalce_odd_numbers(arr):
    return np.where(arr%2!=0, -1, arr)

#repalce_odd_numbers(np.array([1,2,3,4,5,6]))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

def replace_by_value(arr, num):
    return np.where(arr<num, -1, 1)

#replace_by_value(np.array([1, 2, 5, 0]), 2)


# %%
# Készítsd egy olyan függvényt, ami az array értékeit összeszorozza és az eredmény visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

def array_multi(arr):
    
    return None

array_multi(np.array([1,2,3,4]))

# %%
# Készítsd egy olyan függvényt, ami a 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

# %%
# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki:  [[0,0,0,0],
#       [0,1,2,0],
#       [0,3,4,0],
#       [0,0,0,0]]
# add_border()

def add_border(arr):
    return np.pad(arr, 1)

add_border(np.array([[1,2],[3,4]]))

# %%
# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot.
# Be: '2023-03', '2023-04'
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

def list_days(start, end):
    out=[]
    return out

list_days('2023-03', '2023-04')

# %%
# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD
# Be:
# Ki: 2017-03-24 

# %%
# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:00:00 óta.
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()



