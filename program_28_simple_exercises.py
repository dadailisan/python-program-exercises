#sum_two

def sum_two(num1, num2):
    return num1 + num2

assert sum_two(1, 3) == 4

#square a number

def square_num(number):
    return number ** 2

assert square_num(2) == 4

#ODD EVEN 

def even_odd(number):
    return number%2!=0
##    if number % 2 == 0:
##        return 'EVEN'
##    else:
##        return 'ODD'

assert even_odd(10) == False

#Length of string

def len_string(string):
    return len(string)

assert len_string('hello') == 5

#last letter of string

def last_letter(string):
    return string[-1]

assert last_letter('hello') == 'o'

#find biggest number

def bigger(input1, input2):
    if input1 > input2:
        return input1
    else:
        return input2

assert bigger(1, 5) == 5
assert bigger('a', 'c') == 'c'


    
#Find The Biggest Guy(3 inputs)

#SHORTEST COMMAND
def biggest_guy(num1, num2, num3):
    return max(num1, num2, num3)

def biggest_guy2(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
        
assert biggest_guy(1, 3, 2) == 3
assert biggest_guy2(1, 3, 2) == 3



def number_to_choice(number):
    race = {1:'usain', 2:'me', 3:'qazi'}
    return race[number]

def choice_to_number(choice):
    race = {'usain':1, 'me':2, 'qazi':3}
    return race[choice]
