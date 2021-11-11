import pandas as pd

df = pd.read_csv('crimes_quad.csv', index_col='NUM_BO')


is_NaN = df.isnull()

row_has_NaN = is_NaN.any(axis=1)

rows_with_NaN = df[row_has_NaN]


print(rows_with_NaN)
