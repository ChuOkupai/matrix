from matrix import Vector, linear_combination
import unittest

class TestLinearCombination(unittest.TestCase):
	"""This class contains tests for the linear_combination function."""

	def test_empty(self):
		v = linear_combination([], [])
		self.assertEqual(v.values, [])

	def test_example_1(self):
		e1 = Vector([1., 0., 0.])
		e2 = Vector([0., 1., 0.])
		e3 = Vector([0., 0., 1.])
		v = linear_combination([e1, e2, e3], [10., -2., .5])
		self.assertEqual(v.values, [10., -2., .5])

	def test_example_2(self):
		v1 = Vector([1., 2., 3.])
		v2 = Vector([0., 10., -100.])
		v = linear_combination([v1, v2], [10., -2.])
		self.assertEqual(v.values, [10., 0., 230.])
