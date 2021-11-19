import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

postos_df = pd.read_csv('../previa/data/processed/postos.csv', index_col='ID')
crimes_df = pd.read_csv('../previa/data/processed/crimes.csv', index_col='ID')

postos_df = postos_df.sort_values(by="LAT")

#print(postos_df["QUAD"].unique())
crimes_df['freq'] = crimes_df.groupby('QUAD')['QUAD'].transform('count')
crimes_df.drop(crimes_df[crimes_df.freq < 10].index, inplace=True)
crimes_df.drop(['freq'], axis=1, inplace=True)
print(crimes_df.groupby('QUAD').count())

crimes_df.to_csv('data/interim/crimes_novos_quad.csv')

