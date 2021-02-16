'''
Demonstrate the use of the .enumerate() function.
'''
my_list = ["hi", "hello", "hi"]
new_list = []
for i , f in enumerate(my_list):
	new_list.append((i,f))
print(new_list)