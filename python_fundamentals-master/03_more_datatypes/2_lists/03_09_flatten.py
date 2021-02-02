'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
listlen = len(starting_list)
flattened = []
z = 0
while z < listlen:
    for h in starting_list[z]:
        flattened.append(h)
    z += 1

print(flattened)