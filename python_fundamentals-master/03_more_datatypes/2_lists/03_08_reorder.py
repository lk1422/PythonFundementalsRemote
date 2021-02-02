'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

z = 10
num = []
k = 1
oddlist = []
evenlist = []
while z > 0:
    num.append(int(input("Enter a number: ")))
    z -= 1


x = 0
while x != 10:
    evenlist.append(num[x])
    x += 2

while k <= 9:
    oddlist.append(num[k])
    k += 2
evenlist.sort(reverse=True)
print(oddlist + evenlist)
