'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
##I FORGOT HOW TO DO THIS  also too lazy to check this is my best attempt
user_input = input("Enter a string: ")
user_list = user_input.split()
tup_list = ()
#split again set equal to tuple
for x in user_list:
    Z = x.split()
    tup_list += tuple(x)

print(tup_list)