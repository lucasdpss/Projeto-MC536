import pandas as pd

postos_df = pd.read_csv('postos_policiais_geocoded.csv', index_col='id')
crimes_df = pd.read_csv('dados_crimes.csv', index_col='NUM_BO')

postos_df = postos_df.sort_values(by='lat')
print(postos_df)

crimes_df = crimes_df.sort_values(by='LATITUDE')
crimes_df = crimes_df.loc[crimes_df['LATITUDE'] < -23.87]
print(crimes_df)

