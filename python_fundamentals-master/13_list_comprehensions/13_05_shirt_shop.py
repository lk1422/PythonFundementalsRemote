'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]
cart_prod = [f"{h}:{i}" for h in colors for i in sizes]
print(cart_prod)