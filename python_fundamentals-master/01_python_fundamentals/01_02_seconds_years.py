'''

Move the code you previously wrote to calculate how many seconds are in a year into this file.
Then execute it as a script to see the output printed to your console.

'''
sec = 60
minutes_in_hour = 60
hours_in_day = 24
days = 365

seconds_per_year = sec*minutes_in_hour
seconds_per_year = seconds_per_year * hours_in_day
seconds_per_year = seconds_per_year * days

print(seconds_per_year)