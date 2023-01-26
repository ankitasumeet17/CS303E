# File: Benford.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 4/23/21
# Date Last Modified: 4/23/21
# Description of Program: This program verifies Benford's law using the U.S. census data from 2009. It ouputs how many total population values; how many unique population values; and a table of results on the leading digits.

import os.path
import math

def benford():
    # Accept from the user the name of a file, containing the census data
    inp = input("Enter the name of a file of census data: ").strip()

    # If no file of that name exists, print an error message and quit
    if not os.path.isfile(inp):
        print("File does not exist")
        return

    # Empty set to store unique population values
    populations = set()

    # Dictionary for leading digit counts with entries of the form [digit:count]
    leadingDigitCount = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    values = leadingDigitCount.values()

    # Open file and ignore the header
    infile = open(inp , "r")

    # Parse the line to extract the population number
    header = infile.readline()
    line = infile.readline().split()
    while line != []:
        number = line[-1]
        # Add that to the set
        populations.add(number)
        # Get its first digit and increment the count for that digit in the dictionary
        digit = number[0]
        leadingDigitCount[digit] += 1
        line = infile.readline().split()

    # Close the file
    infile.close()

    # Print to terminal
    print("Output written to benford.txt")

    outfile = open("benford.txt" , "w")

    outfile.write("Total number of cities: " + str(sum(values)) + "\n")
    outfile.write("Unique population counts: " + str(len(populations)) + "\n")
    outfile.write("First digit frequency distributions:" + "\n")
    outfile.write("Digit\tCount\tPercentage" + "\n")

    for key in leadingDigitCount:
        outfile.write(str(key) + "\t")
        outfile.write(str(leadingDigitCount[key]) + "\t")
        outfile.write(format(((int(leadingDigitCount[key]) / sum(values)) * 100) , ".1f"))
        outfile.write("\n")

    outfile.close()

benford()
