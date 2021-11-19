import glob
import pandas as pd

file = "CrimesV6.xlsx"

df = pd.read_excel(file)

df = df[df['BAIRRO'].notna()]
df = df[df['HORACORRENCIA'].notna()]
df = df[df['LOGRADOURO'].notna()]
df.to_csv("dados_crimes.csv", index=False, encoding= "utf-16-le")