from random import shuffle
from re import search


def get_time():
    try:
        time = input('Time of signup (hh:mm) -> ')
        assert bool(search(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$', time))
        return time
    except AssertionError:
        print('\nThe time was incorrectly formatted. Please try again.')


def get_date():
    try:
        date = input('Signup date (yyyy-mm-dd) -> ')
        assert bool(search(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$',  date))
        return date
    except AssertionError:
        print('\nThe date was incorrectly formatted. Please try again.')
        return get_date()

    
IN = input('Input file name -> ')
OUT = IN.split('.')[0] + '.out'
REG_DATE = get_date()
REG_TIME = get_time()

with open(IN, 'r') as file:
    in_file = file.read().split('\n')

waiting_list = list()
first_min = list()
for line in in_file:
    # Split the name, email, day and time of their registration                 
    name, email, timestamp = line.split('\t')
    timestamp = timestamp.strip('\n')
    day, time = timestamp.split()
    # Select the people who signed up within the first minute
    if day == REG_DATE and time[:5] == REG_TIME:
        first_min.append((name, email, day, time))
    else:
        waiting_list.append((name, email, day, time))

# Shuffle the people in the raffle list randomly
shuffle(first_min)
data = first_min + waiting_list
    
# Get values for formatting
max_name, max_email = 0, 0
for name, email, day, time in data:
    max_name = max(len(name), max_name)
    max_email = max(len(email), max_email)
    
with open(OUT, 'w') as out_file:
    # Add all the names and email addresses together with their number
    for i, line in enumerate(data):
        name, email, day, time = line
        out_file.write(f'{i+1:<{3}}\t{name:<{max_name}}\t{email:<{max_email}}\n') 

print(f'{OUT} created successfully')
