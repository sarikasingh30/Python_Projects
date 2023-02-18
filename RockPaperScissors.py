# Rock, Paper Scissors Game

import random
li = ["rock", "paper", "scissors"]
t = 0
guessChance = 3
c = 0
while (t < guessChance):
    x = li[random.randint(0, 2)]
    n = input(f'Choose among {li[0]}, {li[1]} and {li[2]}: ')
    n = n.lower()
    if n == x:
        print("Chance-", t+1, "Tie!")
    elif n == "rock":
        if x == "paper":
            print("Chance-", t+1, "You lose!", x, "covers", n)
        else:
            print("Chance-", t+1, "You win!", n, "smashes", x)
            c += 1
    elif n == "paper":
        if x == "scissors":
            print("Chance-", t+1, "You lose!", x, "cut", n)
        else:
            print("Chance-", t+1, "You win!", n, "covers", x)
            c += 1
    elif n == "scissors":
        if x == "rock":
            print("Chance-", t+1, "You lose...", x, "smashes", n)
        else:
            print("Chance-", t+1, "You win!", n, "cut", x)
            c += 1
    else:
        print("That's not a valid play. Check your spelling!")
    t += 1
if (c >= 2):
    print("Hurrah!!! You Won the Match...")
else:
    print("Computer Won...")
