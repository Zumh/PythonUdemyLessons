# This is Rolling Dice Game

import random
min = 1
max = 6

rollAgain = "yes"

while rollAgain == "yes" or rollAgain == "y":
    print ("Rolling the dices...")
    print ("The values are..")
    # First dice
    print (random.randint (min, max))
    # Second dice
    print (random.randint (min, max))
    rollAgain = input("Roll the dices again?")
else:
    print ("Thank you for playing the dicing game")
    
