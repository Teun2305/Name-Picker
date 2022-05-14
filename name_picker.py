# -*- coding: utf-8 -*-
"""
@author: teunh
"""

from random import shuffle
from re import search
from sys import exit

'''
INPUT_FILE_NAME must be a .txt file.
Same goes for the OUTPUT_FILE_NAME

REGISTRATION_DATE is the date of the deadline of the registration
It must be formatted in yyyy-mm-dd.
So the 23rd of May, 2022 would become 2022-05-23.

REGISTRATION_TIME is the time of the deadline.
It must be formatted in hh:mm (24h format).
So a quarter past nine in the moring would become 09:15
And half past six in the evening would become 18:30.
'''

INPUT_FILE_NAME = 'names.txt'
OUTPUT_FILE_NAME = 'list.txt'
assert INPUT_FILE_NAME[-4:] == '.txt', 'FILE_NAME should be a .txt file'
assert OUTPUT_FILE_NAME[-4:] == '.txt', 'OUTPUT_FILE_NAME should be a .txt file'

REGISTRATION_DATE = '2022-05-09'
assert bool(search(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$', 
                   REGISTRATION_DATE)), 'REGISTRATION_DATE is wrongly formatted'

REGISTRATION_TIME = '13:00'
assert bool(search(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$', 
                   REGISTRATION_TIME)), 'REGISTRATION_TIME is wrongly formatted'
    

try:
    f = open(INPUT_FILE_NAME, 'r')
except OSError as ose:
    print(f'An error occured when trying to open the file\n{type(ose)}: {ose}')
    print('Execution interupted')
    exit()
except Exception as exc:
    print(f'An error occured when trying to open the file\n{type(exc)}: {exc}')
    print('Execution interupted')
    exit()
else:
    waiting_list = []
    raffle = []
    for x in f:
        # Split the name, email, day and time of their registration                 
        name, email, timestamp = x.split('\t')
        timestamp = timestamp.replace('\n', '')
        day, time = timestamp.split(' ')
        # Select the people who signed up within the first minute
        if day == REGISTRATION_DATE and time[:5] == REGISTRATION_TIME:
            raffle.append((name, email, day, time))
        # Else add them to the waiting list
        else:
            waiting_list.append((name, email, day, time))
    
    # Shuffle the people in the raffle list randomly
    shuffle(raffle)
    data = raffle + waiting_list
    print('Data read successfully')
finally:
    f.close()
    
# Get values for formatting
max_name, max_email = 0, 0
for name, email, day, time in data:
    max_name = max(len(name), max_name)
    max_email = max(len(email), max_email)
    
try:
    f = open(OUTPUT_FILE_NAME, 'x')
except FileExistsError:
    print(f'A file with the name {OUTPUT_FILE_NAME} already exists.')
    print('Execution interupted')
    exit()
except Exception as exc:
    print(f'An error occured when trying to open the file\n{type(exc)}: {exc}')
    print('Execution interupted')
    exit()
else:
    # Add all the names and email addresses together with their ranking number
    for i, x in enumerate(data):
        name, email, day, time = x
        f.write(f'{i+1:<{3}}\t{name:<{max_name}}\t{email:<{max_email}}\t{day} {time}\n')    
    print(f'{OUTPUT_FILE_NAME} created successfully')
finally:
    f.close()
    
print('Script executed successfully')
