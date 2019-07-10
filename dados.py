import pandas as pd

df = pd.read_csv('pnad2012.csv', index_col=False)
df = df.fillna(df.mean())

df = df[df.race != 0]
df = df[df.race != 8]
df.race = df.race.replace({4:'N', 2:'N', 1:'B', 16:'B'})
df.uf.replace({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17: 'Tocantins', 21: 'Maranhão',
    22: 'Piauí', 23: 'Ceará', 24: 'Rio Grande do Norte', 25: 'Paraíba', 26: 'Pernambuco', 27: 'Alagoas', 28: 'Sergipe', 29: 'Bahia',
    31: 'Minas Gerais', 32: 'Espírito Santo', 33: 'Rio de Janeiro', 35: 'São Paulo', 41: 'Paraná', 42: 'Santa Catarina',
    43: 'Rio Grande do Sul', 50: 'Mato Grosso do Sul', 51: 'Mato Grosso', 52: 'Goiás', 53: 'Distrito Federal',
    }, inplace=True)
df.gender = df.gender.replace({1:'Homem', 2:'Mulher'})

#Agrupa por genero, raça, escolaridade e estado.
def income(gender, race, uf):
    values = df[['gender', 'race', 'uf', 'income']].groupby(['gender','race','uf']).mean()
    renda = values['income'][gender, race, uf]
    return round(renda, 2)