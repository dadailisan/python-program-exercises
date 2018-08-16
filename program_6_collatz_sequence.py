#The Collatz Sequence
number = 0
def collatz(number):
        if number % 2 == 0:
            print(number//2)
        elif number % 2 == 1:
            print(3*number + 1)
while number < 100:
    try:
        print('Enter a number: ')
        number = int(input())
        collatz(number)
    except ValueError:
        print('Error! Kindly input a number.')
