'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
x = []
x = (input("Enter a list of numbers less than 8: "))
x = x.split()
z=0
for y in x:
   x[z] = int(y)
   z+=1
x = sorted(x)
## adds two at a time find len then find how many groups of two can be made. Track what was the last string entered. for final string if the len is less then the num of
## turples  *2 add a zero
lzst = []
tup1 = []
tup2 = []
tup3 = []
tup4 = []




h = len(x) / 2.0
if h != int(h):
    h = int(h) + 1
z = 1
for a in x:
    if z <= 2:
        tup1.append(a)
    elif z <= 4:
        tup2.append(a)
    elif z <= 6:
        tup3.append(a)
    elif z <= 8:
        tup4.append(a)
    z += 1
testlist = [tup1, tup2, tup3, tup4]
for i in testlist:
    if len(i) != 2:
        i.append(0)



tup1 = tuple(tup1)
tup2 = tuple(tup2)
tup3 = tuple(tup3)
tup4 = tuple(tup4)



lzst.append(tup1)
lzst.append(tup2)
lzst.append(tup3)
lzst.append(tup4)
print(lzst)




