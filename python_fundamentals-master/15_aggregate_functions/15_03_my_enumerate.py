'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(x):
	enum_list = []
	raw_index = 0
	for i in x:
		enum_list.append((raw_index, i))
		raw_index += 1






	return enum_list


my_list = ["hi", "hello", "hi"]
new_list = []
for i , f in my_enumerate(my_list):
	new_list.append((i,f))
print(new_list)