from matrix import Vector
import unittest

class TestVector(unittest.TestCase):
	"""This class contains tests for the Vector class."""

	def test_ones(self):
		v = Vector.ones(3)
		self.assertEqual(v.values, [1., 1., 1.])
		self.assertEqual(len(v), 3)

	def test_zeros(self):
		v = Vector.zeros(3)
		self.assertEqual(v.values, [0., 0., 0.])
		self.assertEqual(len(v), 3)

	def test_construct_empty(self):
		v = Vector([])
		self.assertEqual(v.values, [])
		self.assertEqual(len(v), 0)

	def test_construct_with_values(self):
		v = Vector([1., 2., 3.])
		self.assertEqual(v.values, [1., 2., 3.])
		self.assertEqual(len(v), 3)

	def test_construct_with_invalid_values(self):
		with self.assertRaises(TypeError):
			Vector([1, 2, 3., 4])

	def test_vector_add(self):
		u = Vector([2., 3.])
		v = Vector([5., 7.])
		expectedValues = [7., 10.]
		w = u + v
		self.assertEqual(w.values, expectedValues)
		u += v
		self.assertEqual(u.values, expectedValues)

	def test_vector_sub(self):
		u = Vector([2., 3.])
		v = Vector([5., 7.])
		expectedValues = [-3., -4.]
		w = u - v
		self.assertEqual(w.values, expectedValues)
		u -= v
		self.assertEqual(u.values, expectedValues)

	def test_vector_scl(self):
		u = Vector([2., 3.])
		expectedValues = [4., 6.]
		v = u * 2
		self.assertEqual(v.values, expectedValues)
		u *= 2
		self.assertEqual(u.values, expectedValues)

	def test_vector_dot(self):
		zeros = Vector.zeros(2)
		ones = Vector([1., 1.])
		self.assertEqual(zeros.dot(zeros), 0.)
		self.assertEqual(zeros.dot(ones), 0.)
		self.assertEqual(ones.dot(zeros), 0.)
		self.assertEqual(ones.dot(ones), 2.)
		u = Vector([-1., 6.])
		v = Vector([3., 2.])
		self.assertEqual(u.dot(v), 9.)
		self.assertEqual(v.dot(u), 9.)

	def test_vector_norm(self):
		v = Vector.zeros(3)
		self.assertEqual(v.norm_1(), 0.)
		self.assertEqual(v.norm(), 0.)
		self.assertEqual(v.norm_inf(), 0.)

		v = Vector([1., 2., 3.])
		self.assertEqual(v.norm_1(), 6.)
		self.assertAlmostEqual(v.norm(), 3.74165738)
		self.assertEqual(v.norm_inf(), 3.)

		v = Vector([-1., 2.])
		self.assertEqual(v.norm_1(), 3.)
		self.assertAlmostEqual(v.norm(), 2.236067977)
		self.assertEqual(v.norm_inf(), 2.)

	def test_vector_angle_cos(self):
		u = Vector([1., 0.])
		v = Vector([1., 0.])
		self.assertEqual(u.angle_cos(v), 1.)

		v = Vector([0., 1.])
		self.assertEqual(u.angle_cos(v), 0.)

		u = Vector([-1., 1.])
		v = Vector([1., -1.])
		self.assertAlmostEqual(u.angle_cos(v), -1.)

		u = Vector([2., 1.])
		v = Vector([4., 2.])
		self.assertAlmostEqual(u.angle_cos(v), 1.)

		u = Vector([1., 2., 3.])
		v = Vector([4., 5., 6.])
		self.assertAlmostEqual(u.angle_cos(v), 0.974631846)

	def test_vector_cross_product(self):
		u = Vector([0., 0., 1.])
		v = Vector([1., 0., 0.])
		w = u.cross_product(v)
		self.assertEqual(w.values, [0., 1., 0.])

		u = Vector([1., 2., 3.])
		v = Vector([4., 5., 6.])
		w = u.cross_product(v)
		self.assertEqual(w.values, [-3., 6., -3.])

		u = Vector([4., 2., -3.])
		v = Vector([-2., -5., 16.])
		w = u.cross_product(v)
		self.assertEqual(w.values, [17., -58., -16.])

		with self.assertRaises(ValueError):
			u = Vector([1., 2., 3.])
			v = Vector([4., 5.])
			u.cross_product(v)
