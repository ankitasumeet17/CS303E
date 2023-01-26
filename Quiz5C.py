# CS 303E Quiz 5C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Varied Vocabulary
def variedVocabulary(A, B, C):
    sett = []
    for x in A:
        sett.append(x)
    for x in A:
        sett.append(x)
    for x in A:
        sett.append(x)

    sett.pop()

# Problem 2: Gather Grades
def gatherGrades(lst):
    # tuple ('name', g1, g2, g3, g4)
    for i in range(len(lst)-1):
        lowest = 1000
        if lst[i] < lowest:
            lowest = lst[i]

    grade = lst[1] + lst[2] + lst[3] + lst[4] - lowest
    new = {'name1':grade1 , 'name2':grade2 , 'name3':grade3}

    z = 0
    while z < len(lst):
        for x in lst:
            for y in lst[z]:
                studentName = lst[0] 
            z += 1

    return 


if __name__ == "__main__":
    # uncomment the following lines to run the given test cases

    # print(variedVocabulary({'apple', 'orange', 'lemon', 'grape'}, {'banana', 'kiwi', 'strawberry', 'mango'}, {'strawberry', 'lemon', 'orange', 'pineapple', 'kiwi', 'grape'}))
    # print(variedVocabulary({'a', 'b'}, {'c', 'd'}, {'a', 'b', 'c', 'd', 'w'}))
    # print(variedVocabulary({'x', 'y', 'z'}, {'x'}, {'y', 'x'}))

    # print(gatherGrades([("Spongebob", 84, 87, 92, 82), ("Patrick", 25, 30, 20, 25), ("Sandy", 96, 95, 100, 98)]))
    # print(gatherGrades([]))
    # print(gatherGrades([('Squidward', 80, 90, 65, 100), ('Plankton', 20, 20, 100, 20)]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
