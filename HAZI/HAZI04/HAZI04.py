# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
#1
def csv_to_df(utvonal:str) -> pd.core.frame.DataFrame:
    out=pd.read_csv(utvonal)
    return out

#myframe = csv_to_df("StudentsPerformance.csv")
#csv_to_df("StudentsPerformance.csv")

# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
#2
def capitalize_columns(frame:pd.DataFrame) -> pd.core.frame.DataFrame:
    pdf = frame.copy()
    for col in frame.columns:
        if 'e' not in col:
            pdf.rename(columns={col:col.upper()}, inplace=True)
    return pdf

#capitalize_columns(myframe)

# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
#3
def math_passed_count(frame:pd.DataFrame) -> int:
    pdf = frame.copy()
    out=pdf[pdf['math score'] >= 50 ]
    out=out['math score'].count()
    return out

#math_passed_count(myframe)

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
#4
def did_pre_course(frame:pd.DataFrame) -> pd.core.frame.DataFrame:
    pdf = frame.copy()
    out=pdf[pdf['test preparation course'] == 'completed' ]
    return out

#did_pre_course(myframe)

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
#5
def average_scores(frame:pd.DataFrame) -> pd.core.frame.DataFrame:
    pdf = frame.copy()
    #pdf['AVG_score'] = np.average([pdf['math score'], pdf['reading score'], pdf['writing score']])
    #out = pdf.groupby('parental level of education')
    #out = out.aggregate(arg=(np.average(out['math score'] + out['reading score'] + out['writing score'])))

    out = pdf.groupby('parental level of education').mean()
    return out

#average_scores(myframe)

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
#6
def add_age(frame:pd.DataFrame) -> pd.core.frame.DataFrame:
    pdf = frame.copy()
    np.random.seed(42)
    pdf['age'] = np.random.randint(18,67, size=len(pdf))
    return pdf

#add_age(myframe)

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
#7
def female_top_score(frame:pd.DataFrame) -> tuple:
    pdf = frame.copy()
    pdf = pdf[pdf['gender'] == 'female' ]
    pdf['SUM'] = (pdf['math score'] + pdf['reading score'] + pdf['writing score'])
    pdf = pdf.sort_values("SUM").tail(1)
    out = (pdf["math score"].values[0], pdf['reading score'].values[0], pdf['writing score'].values[0])
    return out

#female_top_score(myframe)

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
#8
def add_grade(frame:pd.DataFrame) -> pd.core.frame.DataFrame:
    pdf = frame.copy()
    pdf['percentage'] = ((pdf['math score'] + pdf['reading score'] + pdf['writing score'])/3)
    pdf['grade'] = pdf['percentage'].apply((lambda x: 'F' if x < 60 else ('D' if x < 70 else ('C' if x < 80 else ('B' if x < 90 else ('A' if x >= 90 else None))))))
    return pdf

#add_grade(myframe)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
#9
def math_bar_plot(frame:pd.DataFrame) -> plt.figure:
    pdf = frame.copy()

    fig, ax = plt.subplots()
    group=pdf.groupby(['gender'])
    
    ax.bar(group.groups.keys(),group.mean()['math score'].values)

    ax.set_title("Average Math Score by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Math Score")
    
    return fig

#math_bar_plot(myframe)

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
#10
def writing_hist(frame:pd.DataFrame) -> plt.Figure:
    pdf = frame.copy()

    fig, ax = plt.subplots()
    group=pdf.groupby(['writing score'])
    ax.hist(group['gender'].count())

    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel("Number of Students")
    
    return fig


#writing_hist(myframe)

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
#11
def ethnicity_pie_chart(frame:pd.DataFrame) -> plt.Figure:  
    pdf = frame.copy()

    group=pdf.groupby(['race/ethnicity'])

    fig, ax = plt.subplots()
    ax.set_title("Proportion of Students by Race/Ethnicity")
    ax.pie(group.count()["lunch"].values, labels=group.groups.keys(),autopct='%1.1f%%')
    return fig

#ethnicity_pie_chart(myframe)