'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
number = None
try:
	with open(file_name, 'r') as num:
		j = num.readline()
		j = int(j)


except FileNotFoundError:
	print("File doesnt exist")


except ValueError:
	print("File Input was not a string")
else:
	print(j*8)