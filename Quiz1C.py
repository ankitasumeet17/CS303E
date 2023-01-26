# CS 303E Quiz 1C
# Author: Finn Frankis
from math import sqrt

# Problem 1: Isosceles Triangle Perimeter
def isoscelesTrianglePerimeter():
    # convert incoming values to floats immediately
    side = float(input()) 
    height = float(input())

    area = 2 * side + 2 * sqrt((side ** 2) - (height ** 2)) # calculate area from side length and height using formula
    area_rounded = round(area, 2) # round area to two decimal places

    print("{:.2f}".format(area_rounded)) # print area to two decimal places
    

# Problem 2: Weight Unit Conversion
def weightUnitConversion():
    ounces = int(input()) # convert input ounces to integer

    pounds = ounces // 16 # determine the integer number of pounds in the given number of ounces
    ounces_remaining = ounces % 16 # determine how many ounces are left after the rest have been converted to pounds

    tons = pounds // 2000 # determine the integer number of tons in the remaining number of pounds
    pounds_remaining = pounds % 2000 # determine how many pounds are left after the rest have been converted to tons

    print(tons, pounds_remaining, ounces_remaining)

