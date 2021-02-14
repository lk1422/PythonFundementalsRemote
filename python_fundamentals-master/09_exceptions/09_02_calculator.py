'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
while True:
	dividend = (input("Enter a dividend: "))
	divisor = (input("Enter a divisor: "))
	try:
		int(dividend) and int(divisor)
	except ValueError:
		print("enter a valid number")
	else:
		divisor = int(divisor)
		dividend = int(dividend)

	try:
		print(dividend/divisor)
	except ZeroDivisionError:
		print("Cannot divide by 0")
	except TypeError:
		pass
