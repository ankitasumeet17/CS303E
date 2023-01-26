# File: RecursiveFunctions.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 4/26/21
# Date Last Modified: 4/26/21
# Description of Program: This program calls upon several functions to perform computations that rely on recursion.

def sumItemsInList( L ):
    # Given a list of numbers, return the sum
    if not L:       # L == []
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    # Return the number of times key occurs in list L
    if not L:       # L == []
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] ) # L[1:] excludes first term
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   # Add up the non-negative integers to n
   # E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5
   if n <= 0:
       return 0
   else:
       return n + addToN( n - 1 ) # goes down then back UP

def findSumOfDigits( n ):
   # Return the sum of the digits in a non-negative integer
   if n <= 0:
       return 0
   else:
       return n%10 + findSumOfDigits( n//10 )

def decimalToBinary( n ):
   # Given a nonnegative decimal integer n, return the binary representation as a string
   if n == 0:
       return str(0)
   elif n == 1:
       return str(1)
   else:
       return decimalToBinary( n//2 ) + str(n%2)

def decimalToList( n ):
   # Given a positive decimal integer, return a list of the digits (as strings)
   if n == 0:
       return [str(0)]
   elif 0 < n < 10:
       return [str(n)]
   else:
       return decimalToList( n//10 ) + [str( n%10 )]
       # 3490 --> ['3', '4', '9', '0']

def isPalindrome( s ):
   # Return True if string s is a palindrome and False otherwise
   # Count the empty string as a palindrome
   if len( s ) < 2:
       return True
   elif s[0] != s[-1]:
       return False
   else:
       return isPalindrome( s[1:-1] )

def findFirstUppercase( s ):
   # Return the first uppercase letter in string s, if any
   # Return None if there is none
   if not s:
       return None
   elif chr(65) <= s[0] <= chr(90):
       return s[0]
   else:
       return findFirstUppercase( s[1:] )

def findFirstUppercaseIndexHelper( s, index ):
   # Helper function for findFirstUppercaseIndex
   if not s:
       return -1
   elif index + 1 > len(s):
       return -1
   elif chr(65) <= s[index] <= chr(90):
       return index
   else:
       return findFirstUppercaseIndexHelper( s , index + 1 )

# The following function is already completed for you.  But
# make sure you understand what it's doing.

def findFirstUppercaseIndex( s ):
   # Return the index of the first uppercase letter in string s, if any
   # Return -1 if there is none
   # This one requires a helper function, which is the recursive function
   return findFirstUppercaseIndexHelper( s, 0 )
