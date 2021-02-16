'''
Write a script with a function that demonstrates the use of **kwargs.

'''
def name_age(**kwargs):
	for n, a in kwargs.items():
		print(f"{n} is {a} years young :)")
name_age(joe=10,len=9)