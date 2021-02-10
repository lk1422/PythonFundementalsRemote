'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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
class Bank():
	def __init__(self, dollars, account_type, name ):
		self.dollars = dollars
		self.account_type = account_type
		self.name = name
	def __str__(self):
		return f"{self.name} is a {self.account_type} account and has ${self.dollars} dollars inside of it"
	def __add__(self, other):
		return self.dollars + other.dollars

class Wallet(Bank):
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
	def withdraw(self):
		#amount = int(input("Enter amount withdrawn from the bank: "))
		mock_amount = 100
		self.cash += mock_amount
		self.dollars -= mock_amount
	def deposit(self):
		# amount = int(input("Enter amount withdrawn from the bank: "))
		mock_amount = 100
		self.cash -= mock_amount
		self.dollars += mock_amount
	def spend_cash(self):
		#amount = int(input("Enter amount spent: "))
		mock_amount =  35
		self.cash -= mock_amount
class debt_card(Wallet):
	def __init__(self, dollars, name):
		super().__init__(dollars, name)
	def spend_debt(self):
		# amount = int(input("Enter amount spent: "))
		mock_amount = 35
		self.dollars -= mock_amount
	def availaible_money_in_wallet(self):
		return self.dollars + self.cash
class Book_shelf:
	def __init__(self, number_of_books, total_shelves):
		self.number_of_books = number_of_books
		self.total_shelves = total_shelves
	def __str__(self):
		return f"This Book shelf has {self.number_of_books} books and {self.total_shelves}shelves"
class shelf(Book_shelf):
	def __init__(self, genre, books_contained):
		self.genre = genre
		self.books_contained = books_contained
	def __str__(self):
		return f"This shelf is for the {self.genre} genre and has {self.books_contained} books within it"
class Book(shelf):
	def __init__(self, title, pages, genre):
		self.title = title
		self.pages = pages
		super().__init__(genre)
	def ripped_page(self):
		self.pages -= 1
		self.title = f"Ripped {self.title}"
	def __add__(self, other):
		return self.pages + other.pages
	def __str__(self):
		return f"{self.title} has {self.pages} pages"
