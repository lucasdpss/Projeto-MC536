import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

postos_df = pd.read_csv('../previa/data/processed/postos.csv', index_col='ID')
crimes_df = pd.read_csv('data/interim/crimes_novos_quad.csv', index_col='ID')

latmin = min(postos_df.LAT.min(), crimes_df.LAT.min())
latmax = max(postos_df.LAT.max(), crimes_df.LAT.max())
lonmin = min(postos_df.LON.min(), crimes_df.LON.min())
lonmax = max(postos_df.LON.max(), crimes_df.LON.max())
print(latmin, latmax, lonmin, lonmax)

TAM_QUAD = 0.027027
n_quads_lat = int(np.ceil((latmax - latmin)/TAM_QUAD))
n_quads_lon = int(np.ceil((lonmax - lonmin)/TAM_QUAD))
n_quads = n_quads_lon * n_quads_lat

print(n_quads_lat, n_quads_lon, n_quads)

lats = [latmin + i*TAM_QUAD for i in range(n_quads_lat + 1)]
lons = [lonmin + i*TAM_QUAD for i in range(n_quads_lon + 1)]

quads = {'ID': [], 'LAT_MIN': [], 'LAT_MAX': [], 'LON_MIN': [], 'LON_MAX': []}
for i in range(n_quads_lat):
    for j in range(n_quads_lon):
        quads['ID'].append((i, j))
        quads['LAT_MIN'].append(lats[i])
        quads['LAT_MAX'].append(lats[i+1] - 0.00001)
        quads['LON_MIN'].append(lons[j])
        quads['LON_MAX'].append(lons[j+1] - 0.00001)

quads_df = pd.DataFrame(quads)
quads_df.to_csv('data/interim/quads_novo.csv')
