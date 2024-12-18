import pandas as pd



df_excel = pd.read_excel('excel.xlsx')

print(df_excel.head())

print(df_excel.info())