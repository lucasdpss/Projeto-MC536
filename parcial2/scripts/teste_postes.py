import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

tqdm.pandas()

postes_df = pd.read_csv('postes_quad.csv')

postes_df = postes_df.drop(['LOCAL', 'ID'], axis=1)
postes_df['ID'] = [i for i in range(1, len(postes_df) + 1)]
postes_df.set_index('ID', inplace=True)
print(postes_df)

postes_df.to_csv('postes_final.csv')
