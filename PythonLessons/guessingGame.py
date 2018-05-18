# Description: This is our first number guessing game
# Author: Zumhliansang Lungler
# Date: 30, 2 /2018

import random

def askNumber():
    guessNumber = int(input("Enter an integer from 1 to 99: "))
    return guessNumber

# Defining variables

n = random.randint(1, 99)
guess = askNumber()

# Do a loop
while n != "guess":
    print
    if guess < n:
        print ("Guess number is low")
        guess = askNumber()
    elif guess > n:
        print ("Guess number is high")
        guess = askNumber()
    else:
        print ("You got it!")
        break
    print


