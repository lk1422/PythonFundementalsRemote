'''
Write a script with a function that demonstrates the use of *args.

'''
def my_print(*args):
	for i in args:
		print(i)
text1 = "hi"
lizt_strings = ['test1', 'test2']
my_print(text1, lizt_strings)