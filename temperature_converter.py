def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k * 9/5) - 459.67

# User input
print("Temperature Converter")
value = float(input("Enter the temperature value: "))
scale = input("Enter the scale (C/F/K): ").strip().upper()

if scale == "C":
    print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
    print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")
elif scale == "F":
    print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
    print(f"{value}°F = {fahrenheit_to_kelvin(value):.2f}K")
elif scale == "K":
    print(f"{value}K = {kelvin_to_celsius(value):.2f}°C")
    print(f"{value}K = {kelvin_to_fahrenheit(value):.2f}°F")
else:
       print("Invalid scale! Please enter C, F, or K.")