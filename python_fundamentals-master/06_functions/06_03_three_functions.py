'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
line = input("Enter a line in the form of y = m x + b: ")
# defines the first 10 values of a line 1- 10 finds y int and x int:
def line_converter(n):
	'''
	Input a linear function in form of y = mx + b spaced out as such
	y must be represented as y not a numerical value (must be simplified into this form before hand
	m represents slope
	b represents the y intercept
	the values will be turned out as slope, y int



	'''
	n = n.split()
	n.remove("y")
	n.remove("=")
	n.remove("+")
	n.remove("x")
	slope = int(n[0])
	y_int = int(n[1])
	return [slope , y_int]
def printSlope_yInt():
	x = line_converter(line)
	print("slope = " + str(x[0]) + ", Y-int = " + str(x[1]))
def firsttenpoints(n):
	'''
	finds first 10 points
	'''
	x = line_converter(n)
	slope = x[0]
	y_int = x[1]
	z = 0
	points = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 , 9:0, 10:0}
	for z in range(0,11):
		k = (slope*z) + y_int
		points[z] = k
		z += 1
	return points
print(firsttenpoints(line))


