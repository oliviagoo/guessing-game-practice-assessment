#olivia g 17/3/20
#version 1
#in this version I will check if input is the same as a random number

#importing the random module
import random

#getting and storing random number
num = random.randint(1, 100)

#printing the number for testing
print(num)

#input
guess = int(input("Guess what number I am thinking of: "))

#output
if guess == num:
    print("Correct")
else:
    print("Incorrect")
