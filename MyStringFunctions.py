# File: Student.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 4/2/21
# Date Last Modified: 4/2/21
# Description of Program: This program defines a collection of functions on strings, most of which already exist as methods on the str class.

def myAppend( str, ch ):
    # Return a new string that is like str but with character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears in str
    count = 0
    for i in str:
        if i == ch:
            count = count + 1
    return count

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of str1,
    # followed by the elements of str2, in the same order they appear in str2.
    return str1 + str2

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value" and return None.
    if len(str) == 0:
        print("Empty string: no min value")
        return None

    lowest = 128
    for i in str:
        if ord(i) < lowest:
            lowest = ord(i)
    return chr(lowest)

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been inserted at the ith position.
    # i.e., the string is now one character longer than before.
    # Print "Invalid index" if i is greater than the length of str and return None.
    if i < len(str):
        nstr = str[:i] + ch + str[i:]
        return nstr

    else:
        print("Invalid index")
        return None

def myPop( str, i ):
    # Return two results:
    # 1. a new string that is like str but with the ith element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or equal to len(str), and return str unchanged and None
    if i < len(str):
        nstr = ""
        nstr = str[:i] + str[i+1:]
        return (nstr , str[i])
    else:
        print("Invalid index")
        return (str,None)

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of ch in str, if any.
    # Return -1 if ch does not occur in str.
    for i in range(0 , len(str)):
        if str[i] == ch:
            return i
    return -1

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of ch in str, if any.
    # Return -1 if ch does not occur in str.
    for i in range(len(str)-1, -1, -1):
        if str[i] == ch:
            return i
    return -1

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch removed.
    # If there is none, return str.
    for i in str:
        if i == ch:
            return str[:myFind(str,ch)] + str[myFind(str,ch)+1:]
    return str

def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch removed.
    # If there are none, return str.
    nstr = ""
    for i in str:
        if i != ch:
            nstr = nstr + i

    if nstr == "":
        return str
    else:
        return nstr

def myReverse( str ):
    # Return a new string like str but with the characters in the reverse order.
    nstr = ""
    for i in range(len(str)-1, -1, -1):
        nstr = nstr + str[i]
    return nstr
