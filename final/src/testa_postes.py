import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

tqdm.pandas()

postes_df = pd.read_csv('data/interim/postes_ajustado.csv', index_col='ID')
print(len(postes_df))


#nan_value = float("NaN")
#postes_df.replace("", nan_value, inplace=True)
postes_df.dropna(subset=['QUAD'], inplace=True)
print(len(postes_df))
postes_df.to_csv('data/interim/postes_sem_remotos.csv')
