'''
Print out every prime number between 1 and 100.

'''
prime= []
non_prime = []


h = 2
while h <= 100:
    prime.append(h)
    h += 1




for z in prime[:]:
    for k in range(2, z):
        if z % k == 0 and z != k:
            non_prime.append(z)
            break
for f in non_prime:
    for l in prime:
        if f == l:
            prime.remove(f)
print(prime)
