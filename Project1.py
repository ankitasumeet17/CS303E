# File: Project1.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: February 27, 2021
# Date Last Modified: February 27, 2021
# Description of Program: This program computes a student's semester grade under some simple assumptions.

import math
print()

# student name
studentName = input("Enter the student's name: ")
print()

# input homework
print("HOMEWORKS:")
HW1 = int(input("  Enter HW1 grade: "))
while HW1 < 0 or HW1 > 10:
    print("  Grade must be in range [0..10]. Try again.")
    HW1 = int(input("  Enter HW1 grade: "))
HW2 = int(input("  Enter HW2 grade: "))
while HW2 < 0 or HW2 > 10:
    print("  Grade must be in range [0..10]. Try again.")
    HW2 = int(input("  Enter HW2 grade: "))
HW3 = int(input("  Enter HW3 grade: "))
while HW3 < 0 or HW3 > 10:
    print("  Grade must be in range [0..10]. Try again.")
    HW3 = int(input("  Enter HW3 grade: "))
print()

# input projects
print("PROJECTS:")
P1 = int(input("  Enter Project1 grade: "))
while P1 < 0 or P1 > 100:
    print("  Grade must be in range [0..100]. Try again.")
    P1 = int(input("  Enter Project1 grade: "))
P2 = int(input("  Enter Project2 grade: "))
while P2 < 0 or P2 > 100:
    print("  Grade must be in range [0..100]. Try again.")
    P2 = int(input("  Enter Project2 grade: "))
print()

# input exams
print("EXAMS:")
E1 = int(input("  Enter Exam1 grade: "))
while E1 < 0 or E1 > 100:
    print("  Grade must be in range [0..100]. Try again.")
    E1 = int(input("  Enter Exam1 grade: "))
E2 = int(input("  Enter Exam2 grade: "))
while E2 < 0 or E2 > 100:
    print("  Grade must be in range [0..100]. Try again.")
    E2 = int(input("  Enter Exam2 grade: "))
print()

# calculations
homeworkAverage = 10 * ((HW1 + HW2 + HW3) / 3)
projectAverage = (P1 + P2) / 2
examAverage = (E1 + E2) / 2
hCalc = homeworkAverage * .30
pCalc = projectAverage * .30
eCalc = examAverage * .40
courseAverage = hCalc + pCalc + eCalc

# grading scale
Grade = None
if courseAverage >= 90.0:
    Grade = "A"
elif courseAverage >= 80.0:
    Grade = "B"
elif courseAverage >= 70.0:
    Grade = "C"
elif courseAverage >= 60.0:
    Grade = "D"
else:
    Grade = "F"

# output 
print("Grade report for: " + studentName)
print("  Homework average " + "(30% of grade):" , format(homeworkAverage, ".2f"))
print("  Project average " + "(30% of grade):" , format(projectAverage, ".2f"))
print("  Exam average " + "(40% of grade):" , format(examAverage, ".2f"))
print("  Student course average:" , format(courseAverage, ".2f"))
print("  Course grade " + "(CS303E: Spring, 2021):" , Grade)
print()
