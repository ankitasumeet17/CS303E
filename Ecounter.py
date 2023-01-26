# Exercise 3: Encapsulate this code in a function named count, and
# generalize it so that it accepts the string and the letter as arguments

def example():
    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

def counter():
    user = input('Enter a word: ')
    suser = str(user)
    let = input('Enter a letter to count in this word: ')
    slet = str(let)
    count = 0
    for letter in suser:
        if letter == slet:
            count = count + 1
    print(count)

counter()
