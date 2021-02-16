'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
def sum(x):
	sum = 0
	for i in x:
		sum += i
	return sum
lizt = [1, 2, 3, 4, 5]
print(sum(lizt))