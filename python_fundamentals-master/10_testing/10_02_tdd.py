'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
'''
Functions
-add
-sub
-divide

'''
import unittest
class TestAdd(unittest.TestCase):
	def test_sub(self):
		self.assertEqual(sub(5,3), 2)
class TestSub(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(3,3), 6)
class TestDiv(unittest.TestCase):
	def test_div_equality:
		self.assertEqual(div(3,3), 1)
	def test_errorRaised(self):
		with self.assertRaises(ZeroDivisionError):
			div(3, 0)
