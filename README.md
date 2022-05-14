# Name-Picker

This Python script takes care of the registrations. 
It looks at who registered at what time.
All the people who registered in the first minute will be shuflled randomly.
Then it creates a list based on the new (pseudo-)random order.

## User Manual
First you need the data of the people who registered. 
The attributes which you need are their names, email adresses and time of registration.
These can be found on the CognAC website under Committee Work.
You should copy all the data (without header names) into a simple .txt file.

The easiest way to proceed is placing the .txt file in the same directory as your Python script.
Otherwise you could write out its path.
You should path the name/path of that file under the INPUT_FILE variable.
This variable must be a string.

You do also have to manually set the date and time of the activity's deadline.
The date must be stored under the variable REGISTRATION_DATE in a yyyy-mm-dd format.
The time must bu stored under the variable REGISTRATION_TIME in a hh:mm format.
If you do not follow these formats correctly, the program will raise an assertion error.

The program will create a new .txt file in the same directory as your script.
This file contains the ranking of the participants.
You can change the name of this file under the variable OUTPUT_FILE.

The script won't work if there already exists a file with the same name as your output file in the same directory.
The output file will be a list of all participants with their ranking number.
The places of participants who registered in the first minute will be shuffled.
The other people will receive a higher ranking number based on their order of registration.
