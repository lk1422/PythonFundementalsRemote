'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
sentence = input("Enter a sentence: ")
letter = input("input a letter ton find the occurences of a specifc letter in the string: ")
print(sentence.count(letter))
