try:
    def celsius_to_fahrenheit_kelvin(celsius):
        fahrenheit = (9 / 5 * celsius) + 32
        kelvin = celsius + 273.15
        return fahrenheit, kelvin
except:
        print('Температура должна быть числом')