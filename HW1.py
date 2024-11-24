import math


# номер 4
print('Угол(°) | Синус | Косинус')
print('0|',  round(math.sin(0),4) ,   '|' , round(math.cos(0),4))
print('15|', round(math.sin(15),4) ,  '|' , round(math.cos(15),4))
print('30|', round(math.sin(30),4) ,  '|' , round(math.cos(30),4))
print('45|', round(math.sin(45),4) ,  '|' , round(math.cos(45),4))
print('60|', round(math.sin(60),4) ,  '|' , round(math.cos(60),4))
print('75|', round(math.sin(75),4) ,  '|' , round(math.cos(75,4)))
print('90|', round(math.sin(90),4) ,  '|' , round(math.cos(90),4))



# номер 5
x=int(input('Введите длину первого катета: '))
y=int(input('Введите длину второго катета: '))
z=x*x+y*y
print('Гипотенуза: ',math.sqrt(z))



# номер 6
y=int(input('Введите основное число логарифма: '))
x=int(input('Введите число x: '))
print('Натуральный логарифм: ', round(math.log(x),3))
print('Логарифм по основанию 2: ', round(math.log(x,y),3))
print('Десятичный логарифм: ', round(math.log10(x),3))



# номер 7
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b**2 - 4 * a * c
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Уравнение имеет два корня: x1 = {x1:.1f}, x2 = {x2:.1f}")
elif discriminant == 0:
    x = (-b + math.sqrt(discriminant)) / (2 * a)
    print(f"Уравнение имеет один корень: x = {x:.1f}")
else:
    print("Уравнение не имеет действительных корней.")