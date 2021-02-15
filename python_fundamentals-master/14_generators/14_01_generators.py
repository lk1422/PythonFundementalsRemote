'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
gen = (i for i in range(6))
for z in gen:
	print(z)