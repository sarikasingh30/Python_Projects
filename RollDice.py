import random


def printDice(no):
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")


def num_die():
    while True:
        num_dice = input('Number of dice: ')
        valid_responses = ['1', 'one', 'two', '2']
        if num_dice not in valid_responses:
            raise ValueError('1 or 2 only')
        else:
            return num_dice


def roll_dice():
    min_val = 1
    max_val = 6
    roll_again = 'y'

    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        amount = num_die()

        if amount == '2' or amount == 'two':
            print('Rolling the dice...')
            dice_1 = random.randint(min_val, max_val)
            dice_2 = random.randint(min_val, max_val)
            printDice(dice_1)
            printDice(dice_2)
            print('The values are:')
            print('Dice One: ', dice_1)
            print('Dice Two: ', dice_2)
            print('Total: ', dice_1 + dice_2)

            roll_again = input('Roll Again? ')
        else:
            print('Rolling the die...')
            dice_1 = random.randint(min_val, max_val)
            printDice(dice_1)
            print(f'The value is: {dice_1}')

            roll_again = input('Roll Again? ')


roll_dice()
