# CS 303E Quiz 4C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Condensed Communication
def condensedCommunication(str):
    # replace pass with your solution for Problem 1
    final = ""
    for ch in str:
        if 97 <= ord(ch) <= 122:
            final = final + ch
        elif 65 <= ord(ch) <= 90:
            final = final + ch.lower()
        elif ch.isdigit() == True:
            final = final + ''.join(ch)

    return final.strip()


# Problem 2: Increasing Elements
def increasingElements(lst):
    # replace pass with your solution for Problem 2
    new = []
    new.append(lst[0])
    for i in range(1, len(lst)):
        if lst[i] >= lst[i-1]:
            new.append(lst[i])
    return new

if __name__ == "__main__":
    # uncomment the following lines to run the given test cases

    # print(condensedCommunication("Welp Stacy, I guess you're right. This truly is an ascended form of communication. You're just 3 smart 5 me."))
    # print(condensedCommunication("I wonder how long it will take you to decode this message..."))
    # print(condensedCommunication("Not 0nly is this so hard to understand, but I CAN'T EV3N 3MPHASIZ3 ANYTHING ANYMOR3!!!"))

    # print(increasingElements([29, 15, 13, 20, 21, 1, 29, 6, 27, 28, 1, 6]))
    # print(increasingElements([1, 2, 4, 8, 16]))
    # print(increasingElements([6, 5]))
