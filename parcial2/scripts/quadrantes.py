import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

postos_df = pd.read_csv('postos_policiais_geocoded.csv', index_col='id')
crimes_df = pd.read_csv('dados_crimes.csv', index_col='NUM_BO')

latmin = min(postos_df.lat.min(), crimes_df.LATITUDE.min())
latmax = max(postos_df.lat.max(), crimes_df.LATITUDE.max())
lonmin = min(postos_df.lon.min(), crimes_df.LONGITUDE.min())
lonmax = max(postos_df.lon.max(), crimes_df.LONGITUDE.max())
print(latmin, latmax, lonmin, lonmax)

TAM_QUAD = 0.09009
n_quads_lat = int(np.ceil((latmax - latmin)/TAM_QUAD))
n_quads_lon = int(np.ceil((lonmax - lonmin)/TAM_QUAD))
n_quads = n_quads_lon * n_quads_lat

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
quads_df.to_csv('quads.csv')
