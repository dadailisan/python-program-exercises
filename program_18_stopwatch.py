#! python3
# stopwatch.py - A simple stopwatch program.

import time

#display the program's intructions.
print('Press ENTER to begin.\nAfterwards, press ENTER to "click" the stopwatch.\nPress Ctrl-C to quit.')
input() #press ETER to begin
print('Started.')
start_time = time.time() #get the first lap's start time
last_time = start_time
lap_num = 1

#Start tracking the lap times
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #%s: %s (%s)' %(lap_num, total_time, lap_time), end='')
        lap_num = lap_num + 1 #or lap_num += 1
        last_time = time.time() #reset the last lap time

except KeyboardInterrupt:
    #handle the Ctrl-C excetion to keep its error message from displaying
    print('\nDone!')
    
