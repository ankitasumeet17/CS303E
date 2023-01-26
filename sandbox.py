#seconds = int(input()) # convert input seconds to integer
#minutes = seconds // 60 # determine the int number of minutes
#seconds_remaining = seconds % 60 # determine remainder seconds
#hours = minutes // 60 # determine remaining hours in remainder minutes
#minutes_remaining = minutes % 60 # determine overall remainder minutes
#---------------------------------------------------------------------------------
def sumDigits(n):

    sum = 0
    while n > 0:
        sum = sum + (n % 10) #add the last digit
        n = n // 10 #get rid of last digit

    return sum
#---------------------------------------------------------------------------------
def reverse(n):

    num = n
    digit = 0
    rev = 0
    while num > 0:
        digit = num % 10 # isolate last digit
        rev = rev * 10 + digit # *10 shifts digit to left
        num = num // 10 # reduce n by digit

    return rev # need an ouput to compare

def isPalindrome(n):
    if n == reverse(n): # reverse(n) how you pass n through reverse()
        return True
    else:
        return False
#---------------------------------------------------------------------------------
def displayPattern(n):

    for i in range(1, n+1): # go through each number
        for j in range(1, i+1): # 1, i or 1, 2, i if i is 3 , exclusive
            print(j, end=" ")
        print("")
#---------------------------------------------------------------------------------
def isPrime(n):

    isPrime = True
    if n == 1:
        return False # 1 is not a prime number

    for i in range (2, n):
        if n % i == 0:
            isPrime =  False # if there is even 1 instance of being normal
            break

    return isPrime

def countPrimes(start, end):

    count = 0
    for i in range(start, end+1):
        if isPrime(i) == True:
            count = count + 1

    return count
#---------------------------------------------------------------------------------
# a private string data field named symbol for the stock's symbol
# a private string data field named name for the stock's name
# a private float data field named previousClosingPrice that stores the stock price for the previous day
# a private float data field named currentPrice that stores the stock price for the current time
# a constructor that creates a stock with the specified symbol, name, previous price, and current price
# a get method for returning the stock name
# a get method for returning the stock symbol
# get and set methods for getting/setting the stock's previous price
# get and set methods for getting/setting the stock's current price
# a method named getChangePercent() that returns the precentage changed from previousClosingPrice to currentPrice

class Stock:

    # private data field
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def setPreviousClosingPrice(self, price): # (x , y) for setters
        self.__previousClosingPrice = price

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self, price): # (x , y) for setters
        self.__currentPrice = price

    def getChangePercent(self):
        return (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice * 100 # percentages affected by 100
#---------------------------------------------------------------------------------
class Account:

    def __init__(self, ID=0, balance=100, annualInterestRate=0):
        self.__ID = ID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getBalance(self):
        return self.__balance

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 1200

    def getMonthlyInterest(self):
        return self.__balance * self.__annualInterestRate / 1200

    def deposit(self, int):
        self.__balance = self.__balance + int

    def elapseMonth(self):
        self.__balance = self.__balance + self.__balance * self.__annualInterestRate / 1200
#---------------------------------------------------------------------------------
def daysInYear(year):

    isLeapYear = None
    days = 0

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeapYear = True
            else:
                isLeapYear = False
        else:
            isLeapYear = True
    else:
        isLeapYear = False

    if isLeapYear == True:
        days = 366
    if isLeapYear == False:
        days = 365

    return days

def daysInDecade(startYear):

    total = 0
    for i in range(startYear, startYear+10):
        total = total + daysInYear(i)

    return total
