# CS 303E Exam 1B
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Hexagonal Hex
def hexagonalHex():
    import math
    k = int(input())
    n = 1
    while 0 < k:
        new = n * (2 * n - 1)
        print(new , end = '')
        k = k - 1
       

# Problem 2 - Serendipitous Sum
def serendipitousSum():
    import math
    k = int(input())

    sum = 0
    for i in range (1 , k+1):
        new = ((3 - k) * math.sqrt(k)) ** 3
        sum = sum + new
    print(format(sum , ".2f"))


# Problem 3 - Algorithmic Average
def algorithmicAverage():
    n = int(input())
    pct = 0
    cct = 0
    p = 1
    count = 0
    
    if pct == 0 and cct == 0: 
        for i in range(1 , n + 1):
            if i % 3 == 0:
                count = count + 1
                p = p * i
                pct = pct + 1
                cct = cct + 1
        final = p // count        
        print(format(final , ".1f"))

    else:
        print("0.0")

# Problem 4 - the Wienni Wandering
def theWienniWandering():
    l = int(input())
    a = int(input())
    print(a , end = '')

    for i in range (1 , 5):
        if a > l:
            a = 3 * a - 13
        elif a < 1:
            a = (a // 8) + 12
        elif a == l:
            a = a + 1
        print(a , end = '')
    



# Problem 5 - Coin Calculation
def coinCalculation():
    amt = int(input())
    penny = 1
    nickel = 5
    fdime = 15
    sqtr = 75

    scount = 0
    fcount = 0
    ncount = 0
    pcount = 0
    
    while amt >= 75:
        amt = amt - 75
        scount = scount + 1

    while amt >= 15:
        amt = amt - 15
        fcount = fcount + 1

    while amt >= 5:
        amt = amt - 5
        ncount = ncount + 1

    while amt >= 1:
        amt = amt - 1
        pcount = pcount + 1

    total = scount + fcount + ncount + pcount
    print(total)
    
# Problem 6 - Long Gone Letter
def longGoneLetter():
    let = str(input())
    aScii = chr(ord(let))

    if chr(98) <= aScii <= chr(122) or chr(66) <= aScii <= chr(90):
        print(chr(ord(aScii)-1))
    elif aScii == chr(97) or aScii == chr(65):
        print(chr(ord(aScii)+25))
    
    
# Problem 7 - Hotel Haggling
def hotelHaggling():
    nights = int(input())
    winterb = int(input())

    if nights > 6:
        price = 159 * nights
    elif 3 <= nights <= 6:
        price = 174 * nights
    elif nights <= 2:
        price = 189 * nights

    if winterb == 1:
        price = price * 1.3

    print(format(price , ".2f"))

# Problem 8 - Productive Powers
def productivePowers():
    x = int(input())
    y = int(input())

    if x ** y > 10000:
        print(x * y)
    else:
        print(x ** y)





    
if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    #hexagonalHex()
    #serendipitousSum()
    #algorithmicAverage()
    #theWienniWandering()
    #coinCalculation()
    #longGoneLetter()
    #hotelHaggling()
    #productivePowers()  
    pass
