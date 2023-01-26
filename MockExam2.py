# CS 303E Mock Exam 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Student Class
# DO NOT CHANGE ANYTHING IN THE COURSE CLASS
class Course:
    """A course with a name, professor, and number of credit hours"""
    def __init__(self, name, professor, hours):
        """Create a new course with the given name (a string), professor (a string), and hours (an integer)"""
        self.__name = name
        self.__professor = professor
        self.__hours = hours

    def getName(self):
        """Returns the name of this course"""
        return self.__name

    def getProfessor(self):
        """Returns the professor for this course"""
        return self.__professor

    def getHours(self):
        """Returns the number of credit hours this course counts for"""
        return self.__hours

    def __str__(self):
        """Returns the string representation of this course"""
        return "{} with {}".format(self.__name, self.__professor)

# Complete the Student class below
class Student:
    def __init__(self, name, year, major, courses):
        self.__name = name
        self.__year = year
        self.__major = major
        self.__courses = courses
        self.__hours = 0
        for i in courses:
            course = i
            self.__hours += course.getHours()

    def numCourses(self):
        # replace pass with your numCourses implementation here
        return len(self.__courses)

    def isUpperClassman(self):
        # replace pass with your isUpperClassman implementation here
        if self.__year == 1 or self.__year == 2:
            return False
        else:
            return True

    def totalHours(self):
        # replace pass with your totalHours implementation here
        return self.__hours


    def __str__(self):
        # replace pass with your __str__ implementation here
        if self.__year == 1:
            self.__year = "freshman"
        elif self.__year == 2:
            self.__year = "sophomore"
        elif self.__year == 3:
            self.__year = "junior"
        else:
            self.__year = "senior"

        return (str(self.__name) + " is a " + str(self.__year) + " " + str(self.__major) + " major.")


# Problem 2 - ASCII List to String
def asciiListToString(lst):
    # replace pass with your solution to problem 2 here
    res = ""
    for val in lst:
        res += chr(val)

    return res


# Problem 3 - Essay Character Count
def essayCharacterCount(sentence, words):
    # replace pass with your solution to problem 3 here
    sentence = sentence.split()
    count = 0

    for word in sentence:
        if word.lower() not in words:
            letters = [char for char in word]
            for l in letters:
                count += 1

    return count


# Problem 4 - List of Perfect Squares
def isPerfectSquare(num):
    # replace pass with your isPerfectSquare implementation here
    import math

    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else:
        return False

def listOfPerfectSquares(lst):
    # replace pass with your listOfPerfectSquares implementation here
    new = []
    for i in lst:
        res = isPerfectSquare(i)
        new.append(res)

    return new


# Problem 5 - Character Index Dictionary
def characterIndexDictionary(string):
    # replace pass with your solution to problem 5 here
    letters = [x for x in string]
    dict = {}

    for i in letters:
        dict[str(i)] = letters.index(i)

    return dict


# Problem 6 - Set of Common Factors
def setOfCommonFactors(tup):
    # replace pass with your solution to problem 6 here
    lst = []
    new = set()
    x = 1

    # all values
    for element in tup:
        x = 1
        while x <= element:
            if element % x == 0:
                lst.append(x)
            x += 1

    # add duplicates to set (to return unique factors)
    for i in lst:
        if lst.count(i) == len(tup):
            new.add(i)

    return new



# Problem 7 - Recursive Count Digits
def countDigits(string):
    # replace pass with your solution to problem 7 here
    if string == "":
        return 0
    elif string[0].isdigit() == False:
        return countDigits( string[1:] )
    else:
        return 1 + countDigits( string[1:] )


# Problem 8 - Recursive Divisible by 3 and 5
def divBy3And5(lst):
    # replace pass with your solution to problem 8 here
    if lst == []:
        empty = tuple([0,0])
        return empty
    else:
        divBy3, divBy5 = divBy3And5(lst[1:])
        value = lst[0]
        if (value % 3 == 0):
            divBy3 += 1
        if (value % 5 == 0):
            divBy5 += 1
        divByBoth = tuple([divBy3, divBy5])
        return divByBoth



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases

    # s = Student('Candice', 1, 'Chemistry', [Course('CH 301', 'Laude', 3), \
    #     Course('CS 303E', 'Young', 3), Course('UGS 303', 'Murry', 3), \
    #     Course('M 408C', 'Davis', 4), Course('GOV 310L', 'Moser', 3)])
    # print(s.isUpperClassman())
    # print(s.numCourses())
    # print(s.totalHours())
    # print(str(s))

    # print(asciiListToString([72, 101, 108, 108, 111]))
    # print(asciiListToString([]))
    # print(asciiListToString([123, 116, 114, 51, 51, 32, 37, 33, 125]))

    # print(essayCharacterCount('In conclusion the United States of America is a country', \
    #     {'the', 'a', 'an', 'at', 'but', 'by', 'in', 'for', 'of', 'on', 'to'}))
    # print(essayCharacterCount('Ultimately we shall see that history is not my strongest subject', \
    #     {'this', 'that', 'these', 'those', 'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', \
    #     'him', 'her', 'us', 'them', 'my', 'his', 'hers'}))
    # print(essayCharacterCount('nOne Of thiS actually cOuntS', {'words', 'actually', 'are', \
    #     'none', 'of', 'your', 'business', 'this', 'counts', 'as', 'poetry'}))

    # print(isPerfectSquare(16))
    # print(isPerfectSquare(29))
    # print(listOfPerfectSquares([8, 55, 49, 1, 121, 77, 14, 65, 64, 21, 25, 49]))

    # print(characterIndexDictionary('Hello World!'))
    # print(characterIndexDictionary(''))
    # print(characterIndexDictionary('CS303E is fun CS303E is fun CS303E is fun'))

    # print(setOfCommonFactors((50, 100)))
    # print(setOfCommonFactors((18,)))
    # print(setOfCommonFactors((210, 770, 2730, 1015)))

    # print(countDigits('Ab1cD234EfG56H7'))
    # print(countDigits(''))
    # print(countDigits('CS303E is fun :D'))

    # print(divBy3And5([15, 9, 7, 5, 3]))
    # print(divBy3And5([]))
    # print(divBy3And5([32, 47, -200, 5, 20]))


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
