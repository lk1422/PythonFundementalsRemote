'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
class IntError(Exception):
	pass
x = False
while x == False:
	num = input("Enter a integer: ")
	try:
		num = float(num)
	except ValueError:
		print("This is not a Int")
		print("Enter a Valid Int")
		continue

	if num != int(num):
		try:
			raise IntError("You didn't enter a Int")
		except IntError:
			print("You didn't enter a Int")
			print("Please enter a valid input")
	else:
		print("You entered a integer")
		x = True


