import pandas as pd

pessoas = pd.read_csv('pessoas.csv')
gostos = pd.read_csv('gostos.csv')

def adicionar_gostos(pessoas: list, gostos: list):
    mescla = pd.merge(pessoas, gostos, on='id', how='left')
    mescla = mescla.head().to_dict(orient='records')
    return mescla

mescla = adicionar_gostos(pessoas, gostos)

for pessoa in mescla:
    print (pessoa)