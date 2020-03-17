#olivia g 18/3/20
#version 6
#in this version I will add error handling so my program doesn't break

#importing the random module
import random

#this function forces the user to input e or h
def mode_input(msg):
    while True:
        mode = input(msg).strip().lower()
        if mode == "e":
            guess_num = EASY_GUESS
            break
        elif mode == "h":
            guess_num = HARD_GUESS
            break
        else:
            print("Please enter either E for easy or H for hard mode.")
    return guess_num

#this function forces a number within a 1-100 range
def guess_input(msg):
    while True:
        try:
            guess = int(input(msg))
            if guess > 0 and guess < 101:
                break
            else:
                print("Please enter a guess between 1 and 100.")
        except ValueError:
            print("Please enter a valid whole number.")
    return guess

#setting a guess limit of 10 or 4, depending on the mode
EASY_GUESS = 10
HARD_GUESS = 4

#getting the user to choose what mode they want
guess_num = mode_input("Would you like to play easy mode (10 guesses) or hard mode (4 guesses). Enter E or H: ")

#getting and storing random number
num = random.randint(1, 100)

#printing the number for testing
print(num)

#trying until the user gets it right  or runs out of guesses
while True:
    guess = guess_input("Guess what number I am thinking of: ")
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
