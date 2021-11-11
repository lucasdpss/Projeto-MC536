import pandas as pd
from tqdm import tqdm
import os

tqdm.pandas()

df = pd.read_csv('dados_crimes.csv', index_col='NUM_BO')

arquivos = os.listdir('tipos crimes/')
arquivos.remove('TODOS.txt')

tipos = {}

for arquivo in arquivos:
    tipo = arquivo[:-4]
    tipos[tipo] = []
    with open('tipos crimes/' + arquivo, 'r', encoding='utf8') as f:
        for l in f:
            tipos[tipo].append(l[:-1])

def tipo_crime(rubrica):
    for k in tipos.keys():
        if rubrica in tipos[k]:
            return k

df['TIPO'] = df['RUBRICA'].progress_apply(tipo_crime)
df.to_csv('dados_crimes.csv')

print(df)


