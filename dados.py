import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/EduardoPicolo/desenvolvimento-de-software/master/dados/pad2012.csv", index_col=False)
df = df.fillna(df.mean())

#Media salarial de cada genero
def income_gender():
    values = df[['gender', 'income']].groupby('gender').mean()
    values.rename(columns={'income': 'Renda'}, inplace=True)
    return values

#Agrupa por genero e raça, media salarial de cada raça.
def income_gender_race():
    values = df[['gender', 'race', 'income']].groupby(['gender','race']).mean()
    return(values)