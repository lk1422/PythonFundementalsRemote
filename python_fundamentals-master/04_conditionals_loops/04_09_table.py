'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
z = 0
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []

while z < 50:
    if z < 10:
        row1.append(z)
        z += 1
    elif z < 20:
        row2.append(z)
        z += 1
    elif z < 30:
        row3.append(z)
        z += 1
    elif z < 40:
        row4.append(z)
        z += 1
    else:
        row5.append(z)
        z += 1
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
