#olivia g 17/3/20
#version 2
#in this version I will let the user guess until they get the number right

#importing the random module
import random

#getting and storing random number
num = random.randint(1, 100)

#printing the number for testing
print(num)

#trying until the user gets it right
while True:
    guess = int(input("Guess what number I am thinking of: "))
    if guess == num:
        print("Correct")
        break
    else:
        print("Incorrect")


