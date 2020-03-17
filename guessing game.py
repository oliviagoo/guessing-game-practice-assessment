#olivia g 17/3/20
#version 4
#in this version I will count and limit the number of guesses

#importing the random module
import random

#setting a guess limit of 10, and setting up guess counter
GUESSES = 10
guess_num = GUESSES

#getting and storing random number
num = random.randint(1, 100)

#printing the number for testing
print(num)

#trying until the user gets it right  or runs out of guesses
while True:
    guess = int(input("Guess what number I am thinking of: "))
    if guess == num:
        print("Correct")
        break
    else:
        print("Incorrect")
        guess_num -= 1
        if guess_num > 0:
            if guess < num:
                print("The number is higher!")
            #if the guess isn't the number and isn't lower, it must be higher
            else:
                print("The number is lower!")
        else:
            print("You ran out of guesses!")
            break
