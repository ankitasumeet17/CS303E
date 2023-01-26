#-------------------------------------BEGINNER-------------------------------------
#welcoming the user
name = input("Enter your name: ")
print("Hello, " + name + "! Let's play hangman!")
print("So what's your first guess?")
print()

word = "hello"
guesses = ""
turns = 10

#check if the number of turns are more than zero
while turns > 0:         

    failed = 0
    
    for char in word:      
        if char in guesses:    
          print(char)
        else:
            print("_") 
            failed += 1    

    if failed == 0:        
        print()
        print("You won!")
        break              

    print()
    
    # ask the user go guess a character
    guess = input("guess a character: ") 

    # add the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
        turns -= 1        
        print()
        print("Wrong Guess")    
        print("You have", + turns, 'more guesses')
        print()
        
        if turns == 0:           
            print ("You Lose")
            
#---------------------------------INTERMEDIATE-------------------------------------
import sys
import random

name = input("What is your name?\n")

def run():
  print(f"Hello, {name}, let's play hangman!")
  print("Start guessing...")
  
  #Defining the bag of words
  bag_of_words = ["python", "loop", "code", "control", "exception", "nomalization"]
  word = random.choice(bag_of_words)

  guesses = ""
  turns = 10

  while turns > 0:

    failed = 0
    
    for char in word:
      if char in guesses:
        print(char)
      else:
        print("_")
        failed += 1
        
    if failed == 0:
      print("You win!")
      choice = input("Would you like to play again? Enter y/n\n")
      if "y" in choice:
        run()
      elif "n" in choice:
        sys.exit()
      else:
        print("Something went wrong. Type y or n.")
        
    guess = input("Guess a character: ")
    guesses += guess
    
    if guess not in word:
      turns -= 1
      print("Wrong!")
      print(f"You have {turns} more guesses.")

      if turns == 0:
        print("You lose!")
        print()
        choice = input("Would you like to play again? y/n\n")

        if "y" in choice:
          run()
        elif "n" in choice:
          sys.exit()
        else:
          print("Something went wrong, type y or n.")
run()

#-------------------------------------ADVANCED-------------------------------------
# step 1
!pip install Random-Word

# An example of how it works
# from random_word import RandomWords
# r = RandomWords()
# Return list of Random words
# r.get_random_words()

# step 2
def get_num_attempts():
  while True:
    num_attempts = input('How many incorrect attempts do you want? [1-25] ')
    try:
      num_attempts = int(num_attempts)
      if 1 <= num_attempts <= 25:
        return num_attempts
      else:
        print('{0} is not between 1 and 25'.format(num_attempts))
    except ValueError:
      print('{0} is not an integer between 1 and 25'.format(num_attempts))
      
# step 3
def get_min_word_length():
  while True:
    min_word_length = input('What minimum word length do you want? [4-16] ')
    try:
      min_word_length = int(min_word_length)
      if 4 <= min_word_length <= 16:
        return min_word_length
      else:
        print('{0} is not between 4 and 16'.format(min_word_length))
    except ValueError:
      print('{0} is not an integer between 4 and 16'.format(min_word_length))
      
# step 4
def get_display_word(word, idxs):     
  if len(word) != len(idxs):        
     raise ValueError('Word length and indices length are not the same')     
     displayed_word = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(word)])
     return displayed_word.strip()
    
# step 5
from string import ascii_lowercase
def get_next_letter(remaining_letters):
#Get the user-inputted next letter.
  if len(remaining_letters) == 0:
    raise ValueError('There are no remaining letters')
  while True:
    next_letter = input('Guess a character: ').lower()
    if len(next_letter) != 1:
      print('{0} is not a single character'.format(next_letter))
    elif next_letter not in ascii_lowercase:
      print('{0} is not a letter'.format(next_letter))
    elif next_letter not in remaining_letters:
      print('{0} has been guessed before'.format(next_letter))
    else:
      remaining_letters.remove(next_letter)
    return next_letter

# step 6
def play_hangman():
    """Play a game of hangman.
    At the end of the game, returns if the player wants to retry.
    """
    name = input("What is your name? ")
    print("Hello, " + name, "Let's play hangman!")
    
    # Let player specify difficulty
    print('Starting a game of Hangman...')
    attempts_remaining = get_num_attempts()
    min_word_length = get_min_word_length()

    # Randomly select a word
    print('Selecting a word...')
    word = r.get_random_word(minLength = (min_word_length-1))
    print()

    # Initialize game state variables
    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False

    # Main game loop
    while attempts_remaining > 0 and not word_solved:
        # Print current game state
        print('Word: {0}'.format(get_display_word(word, idxs)))
        print('Attempts Remaining: {0}'.format(attempts_remaining))
        print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))

        # Get player's next letter guess
        next_letter = get_next_letter(remaining_letters)

        # Check if letter guess is in word
        if next_letter in word:
            # Guessed correctly
            print('{0} is in the word!'.format(next_letter))

            # Reveal matching letters
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            # Guessed incorrectly
            print('{0} is NOT in the word!'.format(next_letter))

            # Decrement num of attempts left and append guess to wrong guesses
            attempts_remaining -= 1
            wrong_letters.append(next_letter)

        # Check if word is completely solved
        if False not in idxs:
            word_solved = True
        print()

    # The game is over: reveal the word
    print('The word is {0}'.format(word))

    # Notify player of victory or defeat
    if word_solved:
        print('Congratulations!'+name+ 'You won!')
    else:
        print('Oops'+name+' you were not able to guess the word ')

    # Ask player if he/she wants to try again
    try_again = input('Would you like to try again? [y/n] ')
    return try_again.lower() == 'y'



if __name__ == '__main__':
    while play_hangman():
        print()
