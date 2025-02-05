from turtledemo.penrose import start

import pandas as pd

df_Score = pd.read_excel('Score.xlsx')
print('Что нужно сделать?')
print('1. Вывести всё')
print('2. Вывести строчку')
print('3. Вывести столбик')
print('4. Вывести ячейку')
print('0. Выход')
x = int(input('Введите номер пункта: '))
if x == 1:
    print(df_Score)
elif x == 2:
    x12 = int(input('Введите номер строчки: '))
    print(df_Score.iloc[x12])
elif x == 3:
    print('Столбик 1 - Name')
    print('Столбик 2 - Surname')
    print('Столбик 3 - Score')
    x31 = int(input('Введите номер столбика: '))
    if x31 == 1:
        print(df_Score.iloc[Name])
    elif x31 == 2:
        print(df_Score.iloc[Surname])
    elif x31 == 3:
        print(df_Score.iloc[Score])
elif x == 4:
    x41 = int(input('Введите номер строчки: '))
    x42 = int(input('Введите номер строчки: '))
    print(df_Score.iloc[x41:x42])
elif x == 0:
    exit()
else:
    print('Ошибка')