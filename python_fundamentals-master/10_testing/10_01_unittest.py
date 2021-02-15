'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
tests should pass. Also include a test that does not pass.

NOTE: You can write both the code as well as the tests for it in this single file.
However, feel free to adhere to best practices and separate your tests and the functions you are testing
into different files. Note that you will run into an error when attempting to import this file,
because Python modules can't begin with a number.

'''
import unittest
def divide(x,y):
	return x/y
class TestClass(unittest.TestCase):
	def test_division(self):
		self.assertNotEqual(divide(3,3), 1)
	def test_raisesError(self):
		with self.assertRaises(ZeroDivisionError):
			divide(3,0)
if __name__== '__main__':
	unittest.main()
