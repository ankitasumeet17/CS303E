# File: FindPrimeFactors.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 4/9/21
# Date Last Modified: 4/9/21
# Description of Program: This program recieves a series of arbitrary positive integers and returns, for each, a list of its prime factors.

import math

def isPrime (num):
    # for evens and numbers < 2
    if (num < 2 or num % 2 == 0):
        return (num == 2)

    # for range of odd divisors to square root
    divisor = 3
    while (divisor <= math.sqrt(num)):
        if (num % divisor == 0):
            return False
        else:
            divisor = divisor + 2

    return True

def findNextPrime(num):
    if num < 2:
        return 2

    if num % 2 == 0:
        num = num - 1

    guess = num + 2

    while (not isPrime(guess)):
        guess = guess + 2

    return guess

def factorization(num):
    # store num
    final = num
    # if num prime, return num
    if isPrime(num) == True:
        listOnlyPrime = [num]
        return listOnlyPrime
    # else, print factorization
    else:
        listOfFactors = []
        nextBiggestPrime = num
        d = 2
        while num != 1:
            while num % d == 0:
                listOfFactors.append(d)
                num = num / d
            d = findNextPrime(d)
        return listOfFactors

print("Find Prime Factors: ")
num = int(input("Enter a positive integer (or 0 to stop): "))

while num != 0:
    if num == 1:
        print("  1 has no prime factorization." + "\n")
    if num < 0:
        print("  Negative integer entered. Try again." + "\n")
    if (num > 1 and isPrime(num) == True):
        print("  The prime factorization of " + str(num) + " is: " + str(factorization(num)) + "\n")
    if (num > 1 and isPrime(num) == False):
        print("  The prime factorization of " + str(num) + " is: " + str(factorization(num)) + "\n")
    num = int(input("Enter a positive integer (or 0 to stop): "))

print("Goodbye!" + "\n")
