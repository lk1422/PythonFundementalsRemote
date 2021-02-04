'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
def four_or_seven(n):
    if n%7 or n%4 == 0:
        x = True
    else:
        x = False
    return x
def four_and_seven(n):
    if n%7 and n%4 == 0:
        x =  True
    else:
        x = False
    return x
def num_input():
    x = int(input("Pick a number from 1 - 1,000,000,000"))
    return x

fos = four_or_seven(num_input())
fas = four_and_seven(num_input())
print(fos)
print(fas)
##NOT clear if you wanted me to input the same user input into both or if you wanted me to prompt the user input for both
'''
But so you know i can do it
it would look like this
x = num_input()
fos = four_or_seven(x)
fas = four_and_seven(x)
'''