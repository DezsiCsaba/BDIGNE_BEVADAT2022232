# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt ami a bemeneti dictionary-ből egy DataFrame-et ad vissza.

Egy példa a bemenetre: test_dict
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: dict_to_dataframe
'''

# %%
stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
#1
def dict_to_dataframe(dict) -> pd.core.frame.DataFrame:
    out=pd.DataFrame.from_dict(dict)
    return out

#myframe = dict_to_dataframe(stats)
#print(myframe)

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja csak azt az oszlopot amelynek a neve a bemeneti string-el megegyező.

Egy példa a bemenetre: test_df, 'area'
Egy példa a kimenetre: test_df
return type: pandas.core.series.Series
függvény neve: get_column
'''

# %%
#2
def get_column(frame: pd.DataFrame, colname) -> pd.core.series.Series:
    out=frame.copy()[colname]
    return out

#get_column(myframe, 'area')

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja a két legnagyobb területű országhoz tartozó sorokat.

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: get_top_two
'''

# %%
#3
def get_top_two(frame: pd.DataFrame) -> pd.core.frame.DataFrame:
    area = frame.copy()    
    return (area.sort_values("area").tail(2))

#get_top_two(myframe)

# %%
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből kiszámolja az országok népsűrűségét és eltárolja az eredményt egy új oszlopba ('density').
(density = population / area)

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: population_density
'''

# %%
#4
def population_density(frame:pd.DataFrame) -> pd.core.frame.DataFrame:
    out = frame.copy()
    out['density'] = out['population'] / out['area']
    return out

#population_density(myframe)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlopdiagramot (bar plot),
ami vizualizálja az országok népességét.

Az oszlopdiagram címe legyen: 'Population of Countries'
Az x tengely címe legyen: 'Country'
Az y tengely címe legyen: 'Population (millions)'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_population
'''

# %%
#5
def plot_population(frame:pd.DataFrame) -> plt.figure:
    fr = frame.copy()
    fig, axes = plt.subplots()
    axes.bar(fr['country'], fr['population'])
    axes.set_xlabel("Country")
    axes.set_ylabel("Population (millions)")
    axes.set_title("Population of Countries")
    return fig

#plot_population(myframe)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja az országok területét. Minden körcikknek legyen egy címe, ami az ország neve.

Az kördiagram címe legyen: 'Area of Countries'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_area
'''

# %%
#6
def plot_area(frame:pd.DataFrame) -> plt.figure:
    fr = frame.copy()
    fig, axes = plt.subplots()
    axes.set_title('Area of Countries')
    axes = plt.pie(fr['area'], labels=fr['country'])
    return fig

#plot_area(myframe)


