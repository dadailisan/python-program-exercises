
#message = 'It was a bright cold day in April, and the clocks were striking thirteen
import pprint
while True:
    print('Enter a word/sentence(Enter blank to exit):')
    message = input()
    count = {}
    if message == '':
     break

    else:
        for character in message:
            count.setdefault(character, 0)
            count[character] = count[character] + 1
    pprint.pprint(count)
