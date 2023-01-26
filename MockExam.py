# CS 303E Mock Exam (homework 6)
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Sphere Surface Area
def sphereSurfaceArea():
    import math

    radius = float(input())
    if radius < 0:
        print('Negative radius entered')
    else:
        area = 4 * math.pi * (radius ** 2)
        print(format(area , ".2f"))

# Problem 2: Make Uppercase
def makeUppercase():
    letter = chr(ord(input()))
    if chr(97) <= chr(ord(letter)) <= chr(122):
        print(chr(ord(letter)-32))
    else:
        print(letter)

# Problem 3: Sum Series
def sumSeries():
    num = int(input()
)
    sum = 0
    for i in range(2 , num + 1):
        final = i * (i-1)
        sum = sum + final 

    print(sum)

# Problem 4: Sort Three Integers
def sortThreeIntegers():
    int1 = int(input())
    int2 = int(input())
    int3 = int(input())

    if int1 > int2 and int1 > int3:
        largest = int1
        if int2 > int3:
            middle = int2
            smallest = int3
        else:
            middle = int3
            smallest = int2

    if int2 > int1 and int2 > int3:
        largest = int2
        if int1 > int3:
            middle = int1
            smallest = int3
        else:
            middle = int3
            smallest = int1

    if int3 > int1 and int3 > int2:
        largest = int3
        if int1 > int2:
            middle = int1
            smallest = int2
        else:
            middle = int2
            smallest = int1

    print(smallest, middle, largest)

# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    import math

    sum = 0.0
    number = float(input())

    while number != 0.0:
        if number > 0.0:
            sum = sum + number
        number = float(input())

    if number == 0.0:
        print(format(sum , ".3f"))

# Problem 6: Print Squared Table
def printSquaredTable():
    n = int(input())

    print('  n      n**2')
    print('-------------')
    x = 1
    while x <= n:
        new = n - (n - x)
        sq = new ** 2
        print('{: 3}'.format(new) , '{:9}'.format(sq))
        x = x + 1

# Problem 7: Largest Square
def largestSquare():
    import math
    n = int(input())
    k = math.sqrt(n)
    if k == int(k):
        print(int(k))
    else:
        if int(k) < k:
            print(int(k))

# Problem 8: Collatz Conjecture
def collatzConjecture():
    n = int(input())

    count = 1 


    while n != 1:

        if n%2 == 0:

            n = n//2

            count = count + 1

        if n%2 != 0 and n!= 1:

            n = 3 * n + 1

            count = count + 1

        if n == 1:

            break

    

    print(count)


