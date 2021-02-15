'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
import math
num_list = [i for i in range(1000)]
gen = (i for i in num_list if i % 111 == 0 )
for h in gen:
	print(math.floor(h/1111))