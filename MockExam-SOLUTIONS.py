# CS 303E Mock Exam (homework 6)

import math

# Problem 1: Sphere Surface Area

def sphereSurfaceArea():

    r = float(input())

    # check if the radius is negative
    if r < 0:
        print("Negative radius entered")
    else:
        # use surface area formula to calculate surface area
        surfaceArea = 4 * math.pi * (r ** 2)

        # print the surface area rounded to two decimal places
        print(format(surfaceArea, ".2f"))



# Problem 2: Make Uppercase

def makeUppercase():

    character = input()

    # ord gives us the ASCII code for the character
    asciiCode = ord(character)

    # check if the asciiCode is for a lowercase alphabetical letter
    # The range of values 97 - 122 represent a - z
    if asciiCode >= 97 and asciiCode <= 122:

        # The range of values 65 - 90 represent A - Z
        # if we subtract 32 from the lowercase ASCII value,
        # we get the ASCII code for the same uppercase letter
        
        # chr converts the ASCII code back to a character
        character = chr(asciiCode - 32)
    
    # at this point, character is either capitalized if it was
    # lowercase or unchanged otherwise
    print(character)



# Problem 3: Sum Series

def sumSeries():

    n = int(input())
    sum = 0

    # we want to loop through integers 1, 2, 3, ... , n - 2, n - 1
    # n is not included in this range
    for i in range(1, n):
        # add the current term to the sum
        sum += i * (i + 1)

    # print the sum
    print(sum)



# Problem 4: Sort Three Integers

def sortThreeIntegers():

    numA = int(input())
    numB = int(input())
    numC = int(input())

    # we're just brute forcing this by checking
    # for every possible order for the inputted integers

    if numA <= numB and numA <= numC: # check that numA is the min
        small = numA
        if numB <= numC: # check that numC is the max
            mid = numB
            big = numC
        else: # numB must be the max
            mid = numC
            big = numB
    elif numB <= numA and numB <= numC: # check that numB is the min
        small = numB
        if numA <= numC: # check that numC is the max
            mid = numA
            big = numC
        else: # numA must be the max
            mid = numC
            big = numA
    else: # numC must be the min
        small = numC
        if numA <= numB: # check that numB is the max
            mid = numA
            big = numB
        else: # numA must be the max
            mid = numB
            big = numA

    # by this point, we have found
    # the min, mid, and max

    print(small, mid, big)



# Problem 5: Sum Positive Floats

def sumPositiveFloats():

    # get the first number
    inputVal = float(input())

    total = 0

    # an inputVal of 0 means the end of the input
    while inputVal != 0:
        if inputVal > 0:
            # only add positive floats to the total
            total += inputVal

        # get the next input float
        inputVal = float(input())

    # round to 3 decimal places
    print(format(total, ".3f"))



# Problem 6: Print Squared Table

def printSquaredTable():

    n = int(input())

    # print the labels
    print("  n      n**2")

    # print 13 dashes
    print("-" * 13)

    # we want to loop through values 1, 2, 3, ... , n - 1, n
    # n + 1 is not included in the range
    for i in range(1, n + 1):
        
        # the first number takes a width of 3 and the other 10
        # since 3 + 10 = 13, there should be no extra space between
        # them, so we need to set sep to ""
        print(
            format(i, "3d"),
            format(i**2, "10d"), sep=""
        )


# Problem 7: Largest Square

def largestSquare():

    n = int(input())

    # this is the short way
    # k = math.floor(math.sqrt(n))

    # this is the long way 
    # since n > 0, the smallest possible
    # integer k is 0

    k = 0 

    # we can keep incrementing k as long
    # as the next integer's square is <= n
    while (k + 1) ** 2 <= n:
        k += 1
    print(k)



# Problem 8: Collatz Conjecture

def collatzConjecture():

    term = int(input())

    # the input value starts the sequence
    # so we start with 1 terms
    numberOfTerms = 1
    
    # the sequence ends when the term is 1
    while term != 1:
        if term % 2 == 0:
            # term is even
            term = term / 2
        else:
            # term is odd
            term = 3 * term + 1
        numberOfTerms += 1
    
    print(numberOfTerms)
