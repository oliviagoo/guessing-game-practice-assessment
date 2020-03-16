#olivia g 17/3/20
#version 3
#in this version I will give the user helpful hints about their guess

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
        if guess < num:
            print("The number is higher!")
        #if the guess isn't the number and isn't lower, it must be higher
        else:
            print("The number is lower!")


