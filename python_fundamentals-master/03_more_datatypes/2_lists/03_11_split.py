'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

lol = input("Enter a sentence: ")
list_lol = lol.split()
z = 0
m = ""
for x in list_lol:
    h = list_lol.count(x)
    if h > z:
        z = h
        m = x
print("The string '" + m + "' occured " + str(z) + " times")