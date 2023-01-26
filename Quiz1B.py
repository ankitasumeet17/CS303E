# CS 303E Quiz 1B
# Author: Finn Frankis
from math import sqrt

# Problem 1: Regular Octagon Area
def regularOctagonArea():
    side = float(input()) # convert incoming value to float immediately
    area = 2 * (1 + sqrt(2)) * (side ** 2) # calculate area from side length using formula
    area_rounded = round(area, 2) # round area to two decimal places

    print("{:.2f}".format(area_rounded)) # print area to two decimal places
    

# Problem 2: Time Unit Conversion
def timeUnitConversion():
    seconds = int(input()) # convert input seconds to integer

    minutes = seconds // 60 # determine the integer number of minutes in the given number of seconds
    seconds_remaining = seconds % 60 # determine how many seconds are left after the rest have been converted to minutes

    hours = minutes // 60 # determine the integer number of hours in the remaining number of minutes
    minutes_remaining = minutes % 60 # determine how many minutes are left after the rest have been converted to hours

    print(hours, minutes_remaining, seconds_remaining)

