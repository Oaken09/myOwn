import pandas as pd



df_Score = pd.read_excel('Score.xlsx')

print('Весь DataFrame: ')
print(df_Score)
print('Часть DataFrame: ')
print(df_Score.head())
print('Случайные 5 строк: ')
print(df_Score.sample(5))