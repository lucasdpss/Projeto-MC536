import pandas as pd
from tqdm import tqdm


df = pd.read_csv('crimes.csv', index_col='ID')
tipos = df['TIPO_CRIME'].unique()
df_tipos = pd.DataFrame({'NOME': tipos})
df_tipos.to_csv('tipos_crimes.csv')
