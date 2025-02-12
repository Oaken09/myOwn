import pandas as pd

df_Score = pd.read_excel('50.xlsx')
x = df_Score['Group1'].mean()
print(x)