# Using Time and Calendar module, Print current date and time. Print current month calendar.

import datetime

print('Current datetime: {}'.format(datetime.datetime.now()))
print('Current calender month: {} '.format(str(datetime.datetime.now().month)))
print('Current calender month: {} '.format(str(datetime.datetime.now().strftime("%B"))))

# Using time module perform following operations.
# a) Print current time for every 5 seconds up to 1 minute time interval.
# b) Write a program to find out how much CPU time is taken for the execution of above(32.a)  program.


import time

start_time = time.time()

count = 0
while count <= 60:
    print(datetime.datetime.now())
    time.sleep(5)
    count += 5

print('Total CPU time: {}'.format(time.time() - start_time))
