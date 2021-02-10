'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class Pens():
	def __init__(self, ink, pen_type):
		self.ink = ink
		self.pen_type = pen_type
	def __add__(self, other):
		return self.ink + ", " + other.ink
	def __str__(self):
		if self.ink == "none":
			return f"This pen has no ink and is a {self.pen_type}"
		else:
			return f"This pen has {self.ink} ink and is a {self.pen_type} pen"
	def out_of_ink(self):
		self.ink = "none"
		self.type = f"inkless {self.pen_type}"

class Wallet():
	def __init__(self, cash, color):
		self.cash =  cash
		self.color = color
	def money_in(self):
		#amount =  int(input("How much are you putting into the wallet"))
		mock_amount = 35
		self.cash += mock_amount
	def __add__(self, other):
		return  self.cash + other.cash
	def __str__(self):
		return f"Your {self.color} wallet has ${self.cash} inside of it"

class Book():
	def __init__(self, title, pages):
		self.title = title
		self.pages = pages
	def ripped_page(self):
		self.pages -= 1
		self.title = f"Ripped {self.title}"
	def __add__(self, other):
		return self.pages + other.pages
	def __str__(self):
		return f"{self.title} has {self.pages} pages"

cheap_pen = Pens("blue", "ballpoint")
expenseive_pen = Pens("Black", "Fountain")
cheap_pen.out_of_ink()
print(cheap_pen, expenseive_pen)
colors = cheap_pen + expenseive_pen
print(colors)

kid_wallet = Wallet(24, "green")
adult_wallet = Wallet(233, "Black")
adult_wallet.money_in()
print(adult_wallet, kid_wallet)
total_money = adult_wallet + kid_wallet
print(total_money)

car = Book("Catcher in the Rye", 234)
nef = Book("1984", 328)
nef.ripped_page()
print(car, nef)
total_pages = car + nef
print(total_pages)
