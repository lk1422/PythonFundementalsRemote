'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
num = int(input("Enter a number from 0 - 1,000,000,000: "))
k = 0
z = 500000
m = 1000000
h = 50000000

if k == num:
    print("Your number was 0")
if num < 500000:
    while k <= num:
        if k == num:
            print("Your Number was " + str(k))
            break
        else:
            k += 1
            print(k)
elif num <= 1000000:
    while z <= num:
        if z == num:
            print("your number was " + str(z))
            break
        else:
            print(z)
            z += 1

elif num < 50000000:
    while m <= num:
        if num == m:
            print("Your Number was" + str(m))
            break

        else:
            m += 1
else:
    if num != h and num != h + 1:
        if num % 2 == 0:
            h = num/2
            while h <= num:
                if num == h:
                    print("Your number was" + str(h))
                    break
                else:
                    h += num/2
                    print(h)
        else:

            h += 1

            while h <= num:
                if h == num:
                    print("Your number was" + str(h))
                    break
                else:
                    h += 2
    else:
        if num == h:
            print("Your number is " + str(h))
        else:
            h += 1
            print("your number was " + str(h))
#couldnt really find efficent work around for large numbers other then intervals i dont feel like going any higher. i kinda cheated for even large numbers but odd numbers are annoying because a lot of them can be prime so there isnt a really simple solution










