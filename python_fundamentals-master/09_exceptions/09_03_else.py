'''
Write a script that demonstrates a try/except/else.

'''
#PRINT A STRING A CERTIAN NUMBER OF TIMES
string = input("Enter a string: ")
times = input("Enter a how many times you want it echo'd: ")

try:
	int(times)
except ValueError:
	print("Enter a valid integer")
else:
	times = int(times)
print(string * times)
