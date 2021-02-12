'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
orglist = []
with open('words.txt', 'r') as wordz:
	for k in wordz.readlines():
		orglist.append(k)
orglist.reverse()

with open('wordsreversed.txt', 'w') as lol:
	for j in orglist:
		lol.write(j)
with open('wordsreversed.txt', 'r') as lolr:
	for h in lolr.readlines():
		print(h)