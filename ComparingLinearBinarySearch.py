# File: ComparingLinearBinarySearch.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 4/16/21
# Date Last Modified: 4/16/21
# Description of Program: This code compares the performance of linear and binary search. "Comparing" means seeing on average how many probes (comparisons) are made as you search a list and how closely that average matches the "expected" value.

import math
import random

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

num = list(range(0, 1000))

print("Linear search:")

n = 1
sumL = 0
avgProbesL = 0
for i in range(0,5): # 5 tests being performed
    n = n * 10
    sumL = sumL - sumL # reset sum
    for j in range(n):
        sumL = sumL + (linearSearch(num , random.randint(0,999)) + 1) # add one
    avgProbesL = sumL / n

    print("  Tests: " + format(n,"<9d") + "Average probes: " + str(avgProbesL))

print("Binary search: ")

sumB = 0
biSearch = binarySearch(num , random.randint(0,999))
for i in range(1000):
    sumB = sumB + biSearch[1]

avgProbesB = sumB / 1000
res = math.log(1000,2) - float(avgProbesB)

print("  Average number of probes: " + str(avgProbesB))
print("  Differs from log2(1000) by: " + str(res))
