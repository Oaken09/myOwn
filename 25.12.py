import pandas as pd


df_Score = pd.read_excel('Score.xlsx')
print('Первые 5 строк: ',
      df_Score.head())
print('Последние 5 строк: ',
      df_Score.tail(5))
print('Случайные 5 строк: ',
      df_Score.sample(5))