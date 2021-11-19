import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

tqdm.pandas()

postos_df = pd.read_csv('../previa/data/processed/postos.csv', index_col='ID')

latmin = -23.9480184
lonmin = -46.822750808
TAM_QUAD = 0.027027
lats = [latmin + i*TAM_QUAD for i in range(25)]
lons = [lonmin + i*TAM_QUAD for i in range(23)]

print(lats)
print(lons)

def quad(coord):
    #print(coord[0])
    for i in range(len(lats) - 1):
        if coord[0] >= lats[i] and coord[0] <= lats[i+1]:
            #print(f'i = {i}')
            for j in range(len(lons) - 1):
                if coord[1] >= lons[j] and coord[1] <= lons[j+1]:
                    #print(f'j = {j}')
                    return f'({i}, {j})'

postos_df['QUAD'] = postos_df[['LAT', 'LON']].progress_apply(quad, axis=1)
postos_df.to_csv('data/interim/postos_ajustado.csv')
