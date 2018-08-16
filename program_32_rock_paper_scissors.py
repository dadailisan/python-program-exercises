#Rock, Paper, Scissors GAME!

import random

##CODING WITHOUT DEF FUNCTION
print('THIS IS A ROCK, PAPER and SCISSORS GAME!!!')
print('''1. rock
2. paper
3. scissors''')

rps_dict = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
rps_dict2 = {1 : 'rock', 'paper' : 2, 3 : 'scissors'}
human_score = 0
computer_score = 0
while True:
    print('Whats your pick?')
    human_choice = input()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    convert_h_c = rps_dict[human_choice]
    convert_c_c = rps_dict[computer_choice]
    #RESULTS CHECKING
    #COMPUTER WINS
    if (convert_h_c == 1 and convert_c_c == 2) or (convert_h_c == 2 and convert_c_c == 3)\
         or (convert_h_c == 3 and convert_c_c == 0):
        print('')
        print('YOU LOSE!!!')
        computer_score += 1
        print('Human Score: ', (human_score))
        print('Computer Score: ', (computer_score))
        print('')
    #HUMAN WINS
    elif (convert_h_c == 1 and convert_c_c == 3) or (convert_h_c == 2 and convert_c_c == 0)\
         or (convert_h_c == 3 and convert_c_c == 2):
        print('')
        print('YOU WIN!!!')
        human_score += 1
        print('Human Score: ', (human_score))
        print('Computer Score: ', (computer_score))
        print('')
    #TIE
    else:
        print('')
        print("IT'S A TIE!!!")
        print('Human Score: ', (human_score))
        print('Computer Score: ', (computer_score))
        print('')
