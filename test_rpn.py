import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate('1 1 + 2 +')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3, result)
	def test_mul(self):
		result = rpn.calculate('2 3 *')
		self.assertEqual(6, result)
	def test_pow(self):
		result = rpn.calculate('2 3 ^')
		self.assertEqual(8, result)
	def test_mod(self):
		result = rpn.calculate('15 2 %')
		self.assertEqual(1, result)
	def test_lshift(self):
		result = rpn.calculate('1 2 <<')
		self.assertEqual(4, result)
	def test_rshift(self):
		result = rpn.calculate('4 1 >>')
		self.assertEqual(2, result)
	def test_and(self):
		result = rpn.calculate('2 3 &')
		self.assertEqual(2, result)
	def test_xor(self):
		result = rpn.calculate('2 3 ^^')
		self.assertEqual(1, result)
	def test_invert(self):
		result = rpn.calculate('3 ~')
		self.assertEqual(-4, result)
	def test_or(self):
		result = rpn.calculate('2 3 |')
		self.assertEqual(3, result)
	def test_factorial(self):
		result = rpn.calculate('3 !')
		self.assertEqual(6, result)
