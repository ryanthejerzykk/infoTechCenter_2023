"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""
import sys
# import libraries here
import time

time_to_sleep = 2

print("\nWelcome to the InfoTech Center 2023\n")
time.sleep(time_to_sleep)

# add code to have ellipsis add a dot ever.5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r print a carriage return first so, message is printed on top of the past line
    time.sleep(2.1)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOPERATING SYSTEM LOADING DONE - SCANNED - WELCOME ")



