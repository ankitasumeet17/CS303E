# File: Project2.py
# Student: Ankita Sumeet
# UT EID: as96977
# Course Name: CS303E
#
# Date Created: 4/12/21
# Date Last Modified: 4/12/21
# Description of Program: This program implements a substitution cipher using the SubstitutionCipher class itself, and a main() driver routine which calls it. 

import random

LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey(key):
    # A key is legal if it has length 26 and contains all letters from LCLETTERS
    # returns True or False
    return (len(key) == 26 and all([ch in key for ch in LCLETTERS]))

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS
    newKey = list(LCLETTERS)  # Turn string into list of letters
    random.shuffle(newKey)    # Shuffle the list randomly
    return ''.join(newKey)    # Assemble them back into a string

class SubstitutionCipher:

    def __init__(self, key = makeRandomKey()):
        # Create an instance of the cipher with stored key, which defaults to random.
        self.__key = key

    def getKey(self):
        return self.__key

    def setKey(self, newKey):
        # chk its a legal key
        if isLegalKey(newKey) == True:
            self.__key = newKey

    def encryptText(self, plainText):
        # Return the plaintext encrypted with respect to the stored key.
        sent = ""
        for ch in plainText:
            if 97 <= ord(ch) <= 122: # lowercase
                position = LCLETTERS.index(ch)
                sent = sent + self.__key[int(position)]
            elif 65 <= ord(ch) <= 90: # uppercase
                position = LCLETTERS.index(chr(ord(ch) + 32))
                sent = sent + self.__key[int(position)].upper()
            else:
                sent = sent + ch

        return sent

    def decryptText(self , cipherText):
        # Return the ciphertext decrypted with respect to the stored key.
        sent = ""
        for ch in cipherText:
            if 97 <= ord(ch) <= 122: # lowercase
                position = self.__key.index(ch)
                sent = sent + LCLETTERS[int(position)]
            elif 65 <= ord(ch) <= 90: # uppercase
                position = self.__key.index(chr(ord(ch) + 32))
                sent = sent + LCLETTERS[int(position)].upper()
            else:
                sent = sent + ch

        return sent

def main():
    cipher = SubstitutionCipher()
    # Execute each command as entered.
    inp = input("Enter a command (getkey, changekey, encrypt, decrypt, quit): ").lower()
    while inp != "quit":
        if inp == "getkey":
             # displays the current key stored in cipher
             print("  Current cipher key: " + cipher.getKey())
        elif inp == "changekey":
            # allows the user to change the stored key.
            # The user is given multiple attempts to get this right.
            while True:
                inpCk = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
                if isLegalKey(inpCk) == True:
                    cipher.setKey(inpCk)
                    print("    New cipher key: " + cipher.getKey())
                    break
                elif inpCk == "random":
                    cipher.setKey(makeRandomKey())
                    print("    New cipher key: " + cipher.getKey())
                    break
                elif inpCk == "quit":
                    break
                else:
                    print("    Illegal key entered. Try again!")     

        elif inp == "encrypt":
            # ask user for a text, encrypt it and print the result using the key stored in cipher.
            inpE = input("  Enter a text to encrypt: ")
            print("    The encrypted text is: " + cipher.encryptText(inpE))
        elif inp == "decrypt":
            # ask user for a text, decrypt it and print the result using the key stored in cipher.
            inpD = input("  Enter a text to decrypt: ")
            print("    The decrypted text is: " + cipher.decryptText(inpD))
        else:
            # Anything else: print an error and try again in the outer loop.
            print("  Command not recognized. Try again!")
        inp = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ").lower()
    if inp == "quit":
        # prints a goodbye message (see sample output) and exits the loop
        print("Thanks for visiting!")

main()
