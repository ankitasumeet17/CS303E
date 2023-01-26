#  File: DNA.py

#  Description: This code finds the longest common substring from a pair of DNA sequences.

#  Student Name: Ankita Sumeet

#  Student UT EID: as96977

#  Partner Name: --

#  Partner UT EID: --

#  Course Name: CS 313E

#  Unique Number: A0

#  Date Created: 8/25/21

#  Date Last Modified: 8/29/21

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

import sys

def longest_sub(s1, s2):

    s1Substrings = []
    s2Substrings = []

    s1Substrings = [s1[i: j] for i in range(len(s1)) for j in range(i + 1, len(s1) + 1)]
    s1Substrings = list(set(s1Substrings))

    s2Substrings = [s2[i: j] for i in range(len(s2)) for j in range(i + 1, len(s2) + 1)]
    s2Substrings = list(set(s2Substrings))

    #print(s1Substrings)
    #print(s2Substrings)

    #print(max(s1Substrings))

    s1max = max(s1Substrings)

    longest_sub = []
    for sub1 in s1Substrings:

        for sub2 in s2Substrings:


            if sub2 == sub1 and len(sub1) > len(longest_sub) and len(sub1) > 1:

                longest_sub.append(sub1)

    if (len(longest_sub) == 0):
        finalLongestSub = 'No Common Sequence Found'
        return finalLongestSub

    #print(longest_sub)
    maxLength = max(longest_sub, key = len)
    maxLength = len(maxLength)

    finalLongestSub = []

    for val in longest_sub:
        if len(val) == maxLength:
            finalLongestSub.append(val)

    #print(finalLongestSub)

    return finalLongestSub


#longest_sub('ATGATGGAC', 'GTGATAAGGACCC')
 

def main():
    # read the number of pairs
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int (num_pairs)

    # for each pair call the longest_subsequence
    for x in range (num_pairs):
        st1 = sys.stdin.readline()
        st2 = sys.stdin.readline()

        st1 = st1.strip()
        st2 = st2.strip()

        st1 = st1.upper()
        st2 = st2.upper()

        # get the longest subsequences
        long_sub = longest_sub(st1, st2)

        # print the result
        if type(long_sub) == str:
            print(long_sub)
        else:
            long_sub = sorted(long_sub)
            for sub in long_sub:
                print(sub)
            
    # insert blank line
        print()

if __name__ == "__main__":
    main()