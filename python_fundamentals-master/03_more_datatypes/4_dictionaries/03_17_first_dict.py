'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
x = 1
mydict = {}
while x != 10:
    mydict[x] = x*x
    x += 1
print(mydict)