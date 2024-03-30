# Number Guessing Game
import random


def fun(t, guessChance, x):
    while (t < guessChance):
        n = int(input(f'Enter an integer between {low} and {high}: '))
        if n < x:
            print("The number guessed is low")
        elif (n > x):
            print("The number guessed is high")
        else:
            print(f'The number guessed is right i.e., {x}')
            print("Total chances taken: ", t+1)
            return True
        t += 1
    return False


t = 0
guessChance = 3
low = 1
high = 10
name = input("Hello! What's your Name? ")
print(f'Welcome {name},\n I am choosing a number between {low} and {high}')
x = random.randint(low, high)
print(f'Now your turn to guess the number and you will get only {guessChance} chances')
flag = fun(t, guessChance, x)
if (flag == False):
    print("Oops! Chances over")
replay = input("Do you want to play again?(y/n)")
replay = replay.lower()
newx = random.randint(low, high)
if (replay == "y"):
    fun(t, guessChance, newx)
else:
    exit()
