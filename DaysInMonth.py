# File: DaysInMonth.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: February 15, 2021
# Date Last Modified: February 15, 2021
# Description of Program: This program computes the number of days in a month, given a certain year

# prompt user to input month of year in number format
month = eval(input("Enter a month from 1-12: "))

# assign each number a corresponding month name
if month == 1:
    monthName = "January"
elif month == 2:
    monthName = "February"
elif month == 3:
    monthName = "March"
elif month == 4:
    monthName = "April"
elif month == 5:
    monthName = "May"
elif month == 6:
    monthName = "June"
elif month == 7:
    monthName = "July"
elif month == 8:
    monthName = "August"
elif month == 9:
    monthName = "September"
elif month == 10:
    monthName = "October"
elif month == 11:
    monthName = "November"
else:
    monthName == "December"

# prompt user to input year
year = eval(input("Enter a year: "))

# determine if the entered year is a leap year or not
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            isLeapYear = True
        else:
            isLeapYear = False
    else:
        isLeapYear = True
else:
    isLeapYear = False

# assign the number of days to each month, given whether it is a leap year or not
if isLeapYear: # year is a leap year
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 2:
        days = 29
    else:
        days = 30
else: # year is not a leap year
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 2:
        days = 28
    else:
        days = 30

# final print statement
print(monthName, year, "has" , days , "days")
