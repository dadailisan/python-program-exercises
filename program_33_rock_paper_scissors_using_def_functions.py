#ROCK, PAPER and SCISSOR GAME using DEF FUNCTIONS

import random

def str_to_int(choice):
    rps_dict = {'rock':1, 'paper':2, 'scissors':3}
    return rps_dict[choice] #returns the value of the key[index] wherein index is choice

def human_choice():
    print('What\'s Your Pick?')
    return input()
##    my_choice = input()
##    if my_choice == 'rock' or 'paper' or 'scissors':
##        return my_choice

def computer_choice():
    comp_pick = random.choice(['rock', 'paper', 'scissors'])
    return str_to_int(comp_pick)

def results():
    human_score = 0
    computer_score = 0
    while True:
        human_pick = human_choice()
        num_hp = str_to_int(human_pick)
        num_cp = computer_choice()
##        print(num_hp)
##        print(num_cp)
        #HUMAN WINS
        if (num_hp == 1 and num_cp ==3) or (num_hp == 2 and num_cp == 1)\
           or (num_hp == 3 and num_cp == 2):
            print('\nYOU WIN!!!')
            human_score += 1
            print('\nHuman Score: ', (human_score))
            print('Computer Score: ', (computer_score))
            print('')
        #COMPUTER WINS
        elif (num_hp == 1 and num_cp ==2) or (num_hp == 2 and num_cp == 3)\
           or (num_hp == 3 and num_cp == 0):
            print('\nCOMPUTER WIN!!!')
            computer_score += 1
            print('\nHuman Score: ', (human_score))
            print('Computer Score: ', (computer_score))
            print('')
        else: #num_hp == num_cp
            print('\nIT\'S A TIE!!!')
            print('\nHuman Score: ', (human_score))
            print('Computer Score: ', (computer_score))
            print('')
        print('Press Enter to Continue or Type STOP')
        quit_or_repeat = input()
        if quit_or_repeat == '':
            continue
        elif quit_or_repeat == 'STOP' or 'stop':
            if human_score > computer_score:
                print('YOU WIN THE MATCH!')
            elif human_score < computer_score:
                print('YOU LOSE!!!')
            else:
                print('No one win.')
            break
        else:
            print('You didn\'t press Enter.')
            break

print('THIS IS A ROCK, PAPER, SCISSORS GAME!!!')
print('You\'ll be fighting a computer here.')
results()
print('THANK YOU FOR PLAYING!!!')