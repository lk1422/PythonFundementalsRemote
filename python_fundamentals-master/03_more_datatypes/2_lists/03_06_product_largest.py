'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
i = 10
num = []
h = 0
j = 1
while i > 0:
    num.append(int(input("Enter a number: ")))
    i -= 1
for z in num:
    j *= z
    if z > h:
        h = z
print("The Largest Number Was " + str(h))
print("The product of all the numbers is: " + str(j))
'''
num.sort()
print(num[-1])
I realized i could do this after same result though i tested it........
'''