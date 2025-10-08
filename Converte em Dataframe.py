import pandas as pd
from CombinarGostos import adicionar_gostos

pessoas = pd.read_csv('pessoas.csv')
gostos = pd.read_csv('gostos.csv')

mescla = adicionar_gostos(pessoas, gostos)

def exportar_csv(pessoas: list, nome_arquivo: str):
    df = pd.DataFrame(pessoas)
    df.to_csv(nome_arquivo, index=True)

exportar_csv(mescla, 'pessoas_e_gostos.csv')