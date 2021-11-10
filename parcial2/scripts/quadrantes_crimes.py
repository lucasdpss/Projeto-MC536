import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

tqdm.pandas()

crimes_df = pd.read_csv('dados_crimes.csv', index_col='NUM_BO')

latmin = -23.9480184
lonmin = -49.581026165
TAM_QUAD = 0.09009
lats = [latmin + i*TAM_QUAD for i in range(29)]
lons = [lonmin + i*TAM_QUAD for i in range(39)]

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

crimes_df['QUAD'] = crimes_df[['LATITUDE', 'LONGITUDE']].progress_apply(quad, axis=1)
crimes_df.to_csv('crimes_quad.csv')
