'''
Guessing Game Two
'''

import random

def guessing_game2():
    comp_guess = 0
    try_counter = []
    num_set = True
    while num_set == True:
        try:
            num = int(input("Pick a number from 1 to 100: "))
            print('Good choice!')
            print(num)
            num_set = False
            break
        except:
            print('Invalid input, please choose a number')
    while comp_guess != num:
        comp_guess = random.randint(1,101)
        if comp_guess < num:
            comp_guess = random.randint(1,num)
            try_counter.append(1)
            continue
        elif comp_guess > num:
            comp_guess = random.randint(num,101)
            try_counter.append(1)
            continue
        else:
            try_counter = sum(try_counter)
            print(f'Your number is {num}!')
            print(f'It took {try_counter} attempts to guess your number!')
            comp_guess = 0
            break
    replay_check = input("Would you like to play again, y/n? ").lower()
    if replay_check == 'y':
        guessing_game2()
    else:
        print('Ok, have a nice day!')
if __name__ == '__main__':
    guessing_game2()
    