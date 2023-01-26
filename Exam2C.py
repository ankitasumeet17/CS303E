# CS 303E Exam 2C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: OrgPosition Class
class OrgPosition:
    def __init__(self, name, rank, leadershipPositions):
        # replace pass with your solution to problem 1 here
        self.__name = name
        self.__rank = rank
        self.__leadershipPositions = leadershipPositions

    def updateRanking(self, rank):
        # replace pass with your solution to problem 1 here
        self.__rank = rank

    def numPositions(self):
        # replace pass with your solution to problem 1 here
        return self.__leadershipPositions[0 : int(self.__rank)]

    def getLikelyPosition(self):
        # replace pass with your solution to problem 1 here
        return self.__leadershipPositions[int(self.__rank)-1 : ]

    def __str__(self):
        # replace pass with your solution to problem 1 here
        return (str(self.__name) + " is ranked number " + str(self.__rank) + " in the organization")


# Problem 2: Subtract Corresponding Elements
def subtractLists(lst1, lst2):
    # replace pass with your solution to problem 2 here
    final = [lst1[i] - lst2[i] for i in range(len(lst1))]
    return final
        


# Problem 3: Smaller Letter
def smallerLetter(string):
    # replace pass with your solution to problem 3 here
    x = 0
    i = 0
    new = ""
    letters = [x for x in string]
    for i in range(0, len(letters) , 2):
        if string[x] == string[x + 1]:
            new += str(string[x]) + str(string[x])
        elif ord(string[x]) < ord(string[x + 1]):
            new += str(string[x]) + str(string[x])
        elif ord(string[x]) > ord(string[x + 1]):
            new += str(string[x+1]) + str(string[x+1])

        x += 2

    return new
            


# Problem 4: String List to Dictionary
def stringListToDictionary(s):
    # replace pass with your solution to problem 4 here
    dict = {}
    for i in s:
        new = i.split("-")
        dict[new[0]] = new[1]

    return dict
        


# Problem 5: Set of Common Characters
def commonCharacters(tup):
    # replace pass with your solution to problem 5 here  
    sett = set()
    for i in tup:
        for j in i:
            sett.add(j)
    y = 0
    for x in tup:
        while y < len(tup):
            if tup[x] in sett:
                return sett

            y += 1
    


# Problem 6: Multiple Appearance List
def multipleAppearanceList(lst):
    # replace pass with your solution to problem 6 here
    sett = set()
    for i in lst:
        sett.add(i) # sett has unique val of lst

    this = set(lst) # subtract sets
    res = this - sett 

    if this == []:
        return list(res)
    else:
        if lst == list(sett):
            return list(sett)
        else:
            return lst


# Problem 7: Lagging Lowercase
def laggingLowercase(string):
    # replace pass with your solution to problem 7 here
    if not string:
        return ""
    elif 97 <= ord(string[0]) <= 122:
        if ord(string[0]) == 97:
            return chr(ord(string[0]) + 25) + laggingLowercase(string[1:])
        else:
            return chr(ord(string[0])-1) + laggingLowercase(string[1:])
    else:
        return string[0] + laggingLowercase(string[1:])


# Problem 8: Set of Small Integers
def smallNumbers(lst):
    # replace pass with your solution to problem 8 here
    sett = set()

    if not lst:
        return set()
    else:
        if abs(lst[0]) < 20:
            sett.add(lst[0])
            return sett + smallNumbers(lst[1:])
        else:
            return smallNumbers(lst[1:])

        return sett
            


if __name__ == "__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # s = OrgPosition('Sarah', 3, ['president', 'vice president', 'treasurer', 'secretary', 'social media manager'])
    # s.updateRanking(4)
    # print(str(s))
    # s = OrgPosition('Sarah', 3, ['president', 'vice president', 'treasurer', 'secretary', 'social media manager'])
    # print(s.numPositions())
    # print(s.getLikelyPosition())
    # b = OrgPosition('Bart', 2, ['CEO'])
    # print(b.numPositions())
    # print(b.getLikelyPosition())
    # print(str(b))

    # print(subtractLists([4, 5, 6], [1, 2, 3]))
    # print(subtractLists([], []))
    # print(subtractLists([1, 2, 3], [-1, -2, -3]))

    # print(smallerLetter('aacdfythoopyqt'))
    # print(smallerLetter(''))
    # print(smallerLetter('nnooppee'))

    # print(stringListToDictionary(['1-2', '33-44', '555-666']))
    # print(stringListToDictionary([]))
    # print(stringListToDictionary(['-', 'd-z']))

    # print(commonCharacters(('abcd', 'bcde', 'cdef')))
    # print(commonCharacters(('sooyong',)))
    # print(commonCharacters(('sam', 'kevin', 'sooyong', 'winnie')))

    # print(multipleAppearanceList([1,2,3,4,5]))
    # print(multipleAppearanceList([]))
    # print(multipleAppearanceList([1,1,2,2,3,3]))

    # print(laggingLowercase('aeiou'))
    # print(laggingLowercase(''))
    # print(laggingLowercase('S00y0ng'))

    # print(smallNumbers([1, 2, 3, 4, 5]))
    # print(smallNumbers([]))
    # print(smallNumbers([-21, 10, 20, 30]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
