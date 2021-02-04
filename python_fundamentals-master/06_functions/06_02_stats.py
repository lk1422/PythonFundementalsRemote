'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(n):
    '''
    Takes in a multiple ints or floats
    finds the min max average and sum of the numbers
    returns all of them in a dict
    keys are as followed
    min
    max
    sum
    avg
    '''
    z = 0
    min = 0
    max = 0
    sum = 0
    total = len(n)
    for y in n:
        sum += y
        if z == 0:
            min = y
            z = 1
        if y < min:
            min = y
        if y > max:
            max = y
    avg = sum/ total
    x = {"min": min , "max": max , "sum" : sum , "avg" : avg}
    return x


print(stats(example_list))