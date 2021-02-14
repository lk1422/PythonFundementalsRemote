'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".
'''
import  os
wap = []
with open('C:/Users/lk3on/OneDrive/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/war_and_peace.txt' , 'r' , encoding='utf8') as l:
	for h in l.readlines():
		h = h.rstrip()
		wap.append(h)
with open('C:/Users/lk3on/OneDrive/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/crime_and_punishment.txt', 'w') as k:
	k.write("")
first_line = ''
first_letters = []
for filename in os.listdir('C:/Users/lk3on/OneDrive/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/'):
	directory = 'C:/Users/lk3on/OneDrive/Documents/CodingNomads/labs/python_fundamentals-master/09_exceptions/books/'+filename
	try:
		with open(directory, 'r', encoding='utf8') as lolz:
			first_line = lolz.readline()
			first_letters.append(first_line[0])
	except IndexError:
		print(f"The file {directory} has no text")

print(first_letters)



