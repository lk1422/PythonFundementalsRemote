'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
sentence = input("Enter a sentence: ")
vowela ="a"
vowele = "e"
voweli = "i"
vowelo = "o"
vowelu = "u"

vowels = sentence.count(vowela) + sentence.count(vowele) + sentence.count(voweli) + sentence.count(vowelo) + sentence.count(vowelu)
print(vowels)

print(str(sentence.count(vowela)) + " " + str(sentence.count(vowele)) + " " + str(sentence.count(voweli)) + " "+ str(sentence.count(vowelo)) + " " + str(sentence.count(vowelu)))