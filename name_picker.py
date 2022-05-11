# -*- coding: utf-8 -*-
"""
@author: teunh
"""

from random import shuffle
from re import search

'''
INPUT_FILE_NAME must be a .txt file.
Same goes for the OUTPUT_FILE_NAME
'''
INPUT_FILE_NAME = 'names.txt'
OUTPUT_FILE_NAME = 'list.txt'
assert INPUT_FILE_NAME[-4:] == '.txt', 'FILE_NAME should be a .txt file'
assert OUTPUT_FILE_NAME[-4:] == '.txt', 'OUTPUT_FILE_NAME should be a .txt file'


'''
REGISTRATION_DATE is the date of the deadline of the registration
It must be formatted in yyyy-mm-dd.
So the 23rd of May, 2022 would become 2022-05-23.
'''
REGISTRATION_DATE = '2022-02-30'
assert bool(search(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$', 
                   REGISTRATION_DATE)), 'REGISTRATION_DATE is wrongly formatted'

'''
REGISTRATION_TIME is the time of the deadline, rounded to the nearest second.
It must be formatted in hh:mm:ss.
So a quarter past two in the afternoon would become 14:15:00.
'''
REGISTRATION_TIME = '13:00:00'
assert bool(search(r'^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$', 
                   REGISTRATION_TIME)), 'REGISTRATION_TIME is wrongly formatted'

try:
    # Open the file with the registration data
    f = open(INPUT_FILE_NAME, 'r')
    waiting_list = []
    raffle = []
    for x in f:
        # Split the name, email, day and time of their registration                 
        name, email, timestamp = x.split('\t')
        timestamp = timestamp.replace('\n', '')
        day, time = timestamp.split(' ')
        # If the registration is within one minute after the deadline
        # then select this person for the raffle
        if day == REGISTRATION_DATE and time[:6] == REGISTRATION_TIME[:6]:
            raffle.append((name, email, day, time))
        # Else add them to the waiting list
        else:
            waiting_list.append((name, email, day, time))
    
    # Shuffle the people in the raffle list randomly
    shuffle(raffle)
    data = raffle + waiting_list
    
finally:
    f.close()
    
# Get some values for formatting
max_name, max_email = 0, 0
for name, email, day, time in data:
    max_name = max(len(name), max_name)
    max_email = max(len(email), max_email)
    
try:
    # Create a new .txt file
    f = open(OUTPUT_FILE_NAME, 'x')
    # Add all the names and email addresses together with their ranking number
    for i, x in enumerate(data):
        name, email, day, time = x
        f.write(f'{i+1:<{3}}\t{name:<{max_name}}\t{email:<{max_email}}\t{day} {time}\n')
except FileExistsError:
    print(f'A file with the name {OUTPUT_FILE_NAME} already exists.')
finally:
    f.close()
