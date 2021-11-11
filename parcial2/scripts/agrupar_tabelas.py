import glob
import pandas as pd
import csv
import sys

file_list = glob.glob("D:/Downloads/CSV - Copia/*.tsv")
print(file_list)

all_data = pd.DataFrame()

for f in file_list:
    df = pd.read_csv(f, sep = '\t', encoding = "utf-16-le", lineterminator = '\n',encoding_errors='replace')
    all_data = all_data.append(df, ignore_index=True)


all_data.to_csv('dados_crimes.csv', index=False, encoding= "utf-16-le")
