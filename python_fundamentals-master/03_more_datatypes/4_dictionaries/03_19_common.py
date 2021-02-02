'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict3 = {}
h = False
for x in dict_1.keys():
    h = False
    for y in dict_2.keys():
        if x == y:
            h = True
            dict3[x] = dict_1[x] + dict_2[y]
        else: dict3[y] = dict_2[y]
    if h == False:
        dict3[x] = dict_1[x]
print(dict3)

##ALL VALUES RETURN CORRECT EXCEPT A