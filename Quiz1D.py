# CS 303E Quiz 1D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: Isosceles Triangle Area
def isoscelesTriangleArea():
    import math

    A = float(input())
    B = float(input())

    form = (4*(A**2)) - (B**2)
    area = B/4 * math.sqrt(form)

    print(format(area, ".2f"))





# Problem 2: Volume Unit Conversion
def volumeUnitConversion():
    tbsp = int(input())
    pint = tbsp // 32
    gallon = pint // 8

    print(gallon , pint , tbsp)
