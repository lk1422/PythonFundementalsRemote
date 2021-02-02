'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
x = []
z = 0
while z != 100:
    if z%2 != 0:
        x.append(z)
    z += 1
for y in x:
    print(y)

