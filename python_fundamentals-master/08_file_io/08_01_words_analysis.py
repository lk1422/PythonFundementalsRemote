'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
orlist = []
with open('words.txt', 'r') as wordz:
	for h in wordz.readlines():
		h = h.rstrip()
		orlist.append(h)
shortestlen = 10000000000000000000
longestlen = 0
total = 0
for z in orlist:
	total += 1
	if len(z) < shortestlen:
		shortestlen = len(z)
	if len(z) > longestlen:
		longestlen = len(z)
short_list = []
longest_list = []
for p in orlist:
	if len(p) == shortestlen:
		short_list.append(p)
	elif len(p) == longestlen:
		longest_list.append(p)
print(f"The longest words in the file are {longest_list} \n The shortest words are {short_list}, \n and the total words in the list is {total}")
