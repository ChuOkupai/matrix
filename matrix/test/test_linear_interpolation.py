from matrix import Matrix, Vector, lerp
import unittest

class TestLinearInterpolation(unittest.TestCase):
	"""This class contains tests for the lerp function."""

	def test_lerp_invalid_type(self):
		with self.assertRaises(TypeError):
			lerp(0., 1, 0)

	def test_lerp_float(self):
		self.assertEqual(lerp(0., 1., 0.), 0.)
		self.assertEqual(lerp(0., 1., 1.), 1.)
		self.assertEqual(lerp(0., 1., 0.5), 0.5)
		self.assertEqual(lerp(21., 42., 0.3), 27.3)

	def test_lerp_vector(self):
		u = Vector([2., 1.])
		v = Vector([4., 2.])
		self.assertEqual(lerp(u, v, 0.3).values, [2.6, 1.3])

	def test_lerp_matrix(self):
		u = Matrix([[2., 1.], [3., 4.]])
		v = Matrix([[20., 10.], [30., 40.]])
		self.assertEqual(lerp(u, v, 0.5).values, [[11., 5.5], [16.5, 22.]])
