# номер 2
x=int(input('Введите скорость (в метрах в секунду): '))
y=int(input('Введите время (в секундах): '))
print('Пройденное растояние = ', x*y)



# номер 4
import math


h=int(input('Введите высоту (в метрах): '))
print(round(math.sqrt(2*h/9.8),2))



# номер 5
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
print(round((a+b+c)/3,2))



# номер 8
m=int(input('Введите массу (в килограммах): '))
v=int(input('Введите скорость (в метрах в секунду): '))
print('E = ', round(0.5*m*v**2,2))



# номер 9
x = int(input("Введите угол в градусах: "))
print('Радианы = ', round(x*math.pi/180,2))



# номер 10
x=int(input('Введите  расстояние(в км): '))
y=int(input('Введите скорость (в км/ч): '))
z=x/y
print(round(z, 2))