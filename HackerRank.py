# HackerRank Problems

# -----------------------------------------------------------------
# Celsius to Fahrenheit
try:
    celsius = float(input())
except:
    if celsius >= -273.0:
        print("Invalid input,")
    elif celsius <= 10000.0:
        print("Invalid input")

math = (9/5 * celsius) + 32
Fahrenheit = round(math, 1)
print(Fahrenheit)

# -----------------------------------------------------------------
# Area and Volume
import math

try:
    radius = float(input())
except:
    if radius < 0:
        print("Invalid input")

try:
    length = float(input())
except:
    if length < 0:
        print("Invalid input")

area = math.pi * (radius ** 2)
volume = area * length

Area = format(area, ".2f")
Volume = format(volume, ".2f")

print(Area)
print(Volume)

# -----------------------------------------------------------------
# Calculate tips
import math

subtotal = eval(input())
gratuityRate = eval(input())

if subtotal < 0:
    print("Not in range of possible values")

if gratuityRate < 0:
    print("Not in range of possible values")

gratuityRate = gratuityRate/100
gratuityRate = format(gratuityRate, ".2%")
gratuityRate = gratuityRate.strip()
total = subtotal + (subtotal * gratuityRate)

print(format(gratuity, ".2f"))
print(format(total, ".2f"))
# -----------------------------------------------------------------
