import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

postos_df = pd.read_csv('data/interim/postos_ajustado.csv', index_col='ID')
crimes_df = pd.read_csv('data/interim/crimes_ajustado.csv', index_col='ID')

print(crimes_df.groupby('QUAD').count())
print(postos_df.groupby('QUAD').count())
