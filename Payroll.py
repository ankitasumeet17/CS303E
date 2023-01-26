# File: Payroll.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: Feb 8, 2021
# Date Last Modified: Feb 8, 2021
# Description of Program: this is a program that reads user input and prints a payroll statement

import math

# obtain user information
print(" ")
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
payRate = float(input("Enter hourly pay rate: "))
fedTax = float(input("Enter federal tax withholding rate: "))
stateTax = float(input("Enter state tax withholding rate: "))

# turn decimal inputs into percentages
fw = format(fedTax, "10.1%")
sw = format(stateTax, "10.1%")

# set up deduction equations
fvalue = (hours * payRate) * fedTax
svalue = (hours * payRate) * stateTax
tvalue = fvalue + svalue
nvalue = (hours * payRate) - tvalue

# display calculations
print(" ")
print("Employee Name:" , name)
print("Hours Worked:" , hours)
print("Pay Rate: " + "$" + str(format(payRate , ".2f")))
print("Gross Pay: " + "$" + str(format((hours * payRate) , ".2f")))
print("Deductions: ")
print("  Federal Withholding " + "(" + str(fw.strip()) + "): " + "$" + str(format(fvalue , ".2f")))
print("  State Withholding " + "(" + str(sw.strip()) + "): " + "$" + str(format(svalue , ".2f")))
print("  Total Deduction: " + "$" + str((format(tvalue , ".2f"))))
print("Net Pay: " + "$" + str(format(nvalue , ".2f")))
