# File: MinMax.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: February 22, 2021
# Date Last Modified: February 22, 2021
# Description of Program: This is a program that accepts an arbitrary number of integer inputs from the user and prints out the minimum and maximum of the numbers entered.

# initial input statement
number = input("Enter an integer or 'stop' to end: ")

# statement to determine whether to continue asking for user input
if number == "stop":
    print("You didn't enter any numbers")
else:
    # convert input into an integer and assign min/max values
    number = int(number)
    min = number
    max = number
    while True:
        number = input("Enter an integer or 'stop' to end: ")
        if number != "stop":
            number = int(number)
            # update the min/max values
            if number < min:
                min = number
            if number > max:
                max = number
        else:
            # upon recieving the "stop" input, print the min/max value from all integers entered
            print("The maximum is" , max)
            print("The minimum is" , min)
            # terminate the loop
            break
