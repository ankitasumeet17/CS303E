# File: Student.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 3/26/20
# Date Last Modified: 3/26/20
# Description of Program: This program defines a simple Student class, where a name and two grades are supplied in order to produce an exam average.

class Student:

    def __init__(self, name, examOne = None, examTwo = None):
        self.__name = name
        self.__examOne = examOne
        self.__examTwo = examTwo

    def __str__(self):
        return "Student: " + str(self.__name) + "\n" + \
                " Exam 1: " + str(self.__examOne) + "\n" + \
                " Exam 2: " + str(self.__examTwo)

    def getName(self):
        return self.__name

    def getExam1Grade(self):
        return self.__examOne

    def getExam2Grade(self):
        return self.__examTwo

    def setExam1Grade(self , examOne):
        self.__examOne = examOne

    def setExam2Grade(self , examTwo):
        self.__examTwo = examTwo

    def getAverage(self):
        if self.__examOne == None or self.__examTwo == None:
            print("Some exam grades not available.")
        else:
            return (self.__examOne + self.__examTwo) / 2
