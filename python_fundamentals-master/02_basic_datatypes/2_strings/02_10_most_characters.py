'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
string3 = input("Enter string 3: ")
len1 = str(len(string1))
len2 = str(len(string2))
len3 = str(len(string3))
print(len1 + ", " + string1)
print(len2 + ", " +string2)
print(len3 + ", " + string3)

stringlist= [string1, string2, string3]
longest= max(stringlist, key=len)
print(longest)

