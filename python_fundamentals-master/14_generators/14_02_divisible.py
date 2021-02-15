'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
num_list = [i for i in range(1000)]
gen = (i for i in num_list if i % 111 == 0 )
for j in gen:
	print(j)