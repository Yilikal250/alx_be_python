FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = float(input("Enter the temperature to convert: "))
tempchoose=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if tempchoose == "F":
   print(convert_to_celsius(temp),"°F")
else:
   print(convert_to_fahrenheit(temp),"°C")    