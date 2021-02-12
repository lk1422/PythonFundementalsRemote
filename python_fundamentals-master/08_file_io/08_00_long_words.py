'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
orginlist = []
with open('words.txt', 'r') as wordz:
	for h in wordz.readlines():
		orginlist.append(h)
longwords = []
for z in orginlist:
	if len(z) >= 20:
		print(z)
