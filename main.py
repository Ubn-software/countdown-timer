last_modification = "01/03/2022 | 21:07" 

import time
import datetime
from termcolor import colored

print(colored("""
 _   _ _              __
| | | | |__  _ __    / / Timer 
| | | | '_ \| '_ \  / /  version 1.0
| |_| | |_) | | | |/ /_  
 \___/|_.__/|_| |_/_/(_) Software
""", 'yellow'))

print(colored("Author: @Ubn | https://www.instagram.com/f6a9g1k0/ \n", 'yellow'))

print(colored("Last Modify: " + last_modification + "\n", 'red'))

print(colored("[?] Use CTRL + C to close \n" + "[?] Use an 0 to leave empty \n", 'green'))

def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    print(colored("Times over \n" + "[!] Countdown ended!", 'red'))
 
# Inputs for hours, minutes, seconds on timer
h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))