# File: Project3.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 5/1/21
# Date Last Modified: 5/1/21
# Description of Program: Building a Query Processing Utility --

import os.path
import math

def covid():
    # Dictionary for { countyName: (confirmedCases, deaths) }
    countyName = str()
    confirmedCases = int()
    deaths = int()

    dict = {}

    # Empty list to store unique county names
    counties = []

    # count confirmed cases and deaths
    ccCount = 0
    dCount = 0

    # Open file and ignore the header
    infile = open( "county-covid-data.txt" , "r")

    # Parse the lines
    line = infile.readline()

    while line != "":
        if line[0] != '#':
            line = line.strip().split(",")
            cName = str(line[0])
            # Add counties to list
            counties.append(cName)
            # Get countyName and tuple of confirmedCases and deaths
            confirmedCases = int(line[1])
            probableCases = int(line[2])
            deaths = int(line[3])
            dict[str(cName)] = (confirmedCases , deaths)
            # increment count
            ccCount += confirmedCases
            dCount += deaths
        line = infile.readline()

    # adding dict1 {texas : (total cases, total deaths)} to dict
    dict['Texas'] = (ccCount , dCount)

    # Close the file
    infile.close()

    # return dictionary and list
    return dict, counties

def main():

    dict, counties = covid()

    # Accept from the user the name of a file, containing the census data
    # inp = input("Enter the name of a file of census data: ").strip()

    # If no file of that name exists, print an error message and quit
    # if not os.path.isfile(inp):
        # print("File 'county-covid-data.txt' not found.")
        # return

    # Execute each command as entered
    print()
    print("Welcome to the Texas Covid Database Dashboard.\nThis provides Covid data in Texas as of 1/26/21.\nCreating dictionary from file: county-covid-data.txt\n")
    print("Enter any of the following commands: \n"\
    "\033[1mHelp\033[0m - list available commands;\n"\
    "\033[1mQuit\033[0m - exit this dashboard;\n"\
    "\033[1mCounties\033[0m - list all Texas counties;\n"\
    "\033[1mCases <countyName>/Texas\033[0m - confirmed Covid cases in specified county or statewide;\n"\
    "\033[1mDeaths <countyName>/Texas\033[0m - Covid deaths in specified county or statewide.\n")

    inp = input("\033[1mPlease enter a command: \033[0m")

    # parse the command
    commWords = inp.split()
    # extract the first word
    comm = commWords[0]
    # Extract the rest of the words and re-assemble them into a single string, separated by spaces
    args = commWords[1:]
    arg = " ".join(args)

    while comm.lower() != 'quit':
        if comm.lower() == 'help':
            print("\n\033[1mHelp\033[0m - list available commands;\n"\
            "\033[1mQuit\033[0m - exit this dashboard;\n"\
            "\033[1mCounties\033[0m - list all Texas counties;\n"\
            "\033[1mCases <countyName>/Texas\033[0m - confirmed Covid cases in specified county or statewide;\n"\
            "\033[1mDeaths <countyName>/Texas\033[0m - Covid deaths in specified county or statewide.\n")

        elif comm.lower() == 'counties':
            for i in range((len(counties)//10) + 1):
                print (", ".join(counties[i*10:(i+1)*10]) + "\n")


        elif comm.lower() == 'cases':
            tup = dict.get(arg.title() , None)

            if arg.title() != 'Texas':
                if arg.title() in counties:
                    print (str(arg.title()) + " county has " + str(tup[0]) + " confirmed Covid cases.\n")
                else:
                    print("County " + str(arg) + " is not recognized.\n")
            elif arg.title() == 'Texas':
                print ("Texas total confirmed Covid cases: " + str(tup[0]) + "\n")


        elif comm.lower() == 'deaths':
            tup = dict.get(arg.title() , None)

            if arg.title() != 'Texas':
                if arg.title() in counties:
                    print (str(arg.title()) + " county has " + str(tup[1]) + " fatalities.\n")
                else:
                    print("County " + str(arg) + " is not recognized.\n")
            elif arg.title() == 'Texas':
                print ("Texas total confirmed Covid cases: " + str(tup[1]) + "\n")


        else:
            print("Command is not recognized.  Try again!\n")

        inp = input("\033[1mPlease enter a command: \033[0m")
        # parse the command
        commWords = inp.split()
        # extract the first word
        comm = commWords[0]
        # Extract the rest of the words and re-assemble them into a single string, separated by spaces
        args = commWords[1:]
        arg = " ".join(args)


    print("Thank you for using the Texas Covid Database Dashboard. Goodbye!\n")
    return


main()
