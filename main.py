#номер 1
def say_hi(user_name):
    print(f'Hello {user_name}!')
say_hi('Bob')



#номер 2
def eval(num):
    return num%2==0
print(eval(10))



#номер 3
def find_min(numbers):
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number
numbers = [3,7,2,9,5,0,1,4,6,8]
print(find_min(numbers))



#номер 4
def factorial(num):
    factorial=1
    for i in range(2, num+1):
        factorial *= i
    return factorial
num = int(input())
print(factorial(num))



#номер 5
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
num = int(input())
print(factorial(num))



#номер 6
import math
print(math.factorial(1000))



#номер 7
try:
    def celsius_to_fahrenheit_kelvin(celsius):
        fahrenheit = (9 / 5 * celsius) + 32
        kelvin = celsius + 273.15
        return fahrenheit, kelvin
except:
        print('Температура должна быть числом')