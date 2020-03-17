#olivia g 18/3/20
#version 5
#in this version I will add easy and hard modes

#importing the random module
import random

#setting a guess limit of 10 or 4, depending on the mode
EASY_GUESS = 10
HARD_GUESS = 4

#getting the user to choose what mode they want
mode = input("Would you like to play easy mode (10 guesses) or hard mode (4 guesses). Enter E or H: ").strip().lower()
if mode == "e":
    guess_num = EASY_GUESS
else:
    guess_num = HARD_GUESS

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
