'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

sentence = input("Write a sentece: ")
symbol = input("Choose a symbol: ")

first = sentence[0]
print(sentence.replace(first, symbol))