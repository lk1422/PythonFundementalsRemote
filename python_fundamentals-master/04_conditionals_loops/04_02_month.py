'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
month = int(input("Give a the numerical value for a desired month: "))
if month == 1:
    print("jamuary")
elif month ==2:
    print("Febuary")
elif month == 3:
    print("march")
elif month == 4:
    print("april")
elif month == 5:
    print("may")
elif month == 6:
    print("June")
elif month == 7:
    print("july")
elif month == 8:
    print("august")
elif month == 9:
    print("September")
elif month == 10:
    print("october")
elif month == 11:
    print("november")
else:
    print("January")