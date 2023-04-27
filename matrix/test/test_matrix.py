from matrix import Matrix, Vector
import unittest

class TestMatrix(unittest.TestCase):
	"""This class contains tests for the Matrix class."""

	def test_identity(self):
		m = Matrix.identity(3)
		self.assertEqual(m.values, [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
		self.assertEqual(m.shape, (3, 3))

	def test_construct_empty(self):
		m = Matrix([])
		self.assertEqual(m.values, [])
		self.assertEqual(m.shape, (0, 0))

	def test_construct_with_values(self):
		m = Matrix([[1., 2., 3.], [4., 5., 6.]])
		self.assertEqual(m.values, [[1., 2., 3.], [4., 5., 6.]])
		self.assertEqual(m.shape, (2, 3))

	def test_construct_with_invalid_values(self):
		with self.assertRaises(TypeError):
			Matrix([[1, 2], [3, 4.]])

	def test_construct_with_invalid_shape(self):
		with self.assertRaises(ValueError):
			Matrix([[1, 2], [3, 4, 6]])

	def test_matrix_add(self):
		u = Matrix([[1., 2.], [3., 4.]])
		v = Matrix([[7., 4.], [-2., 2.]])
		expectedValues = [[8., 6.], [1., 6.]]
		w = u + v
		self.assertEqual(w.values, expectedValues)
		u += v
		self.assertEqual(u.values, expectedValues)

	def test_matrix_sub(self):
		u = Matrix([[1., 2.], [3., 4.]])
		v = Matrix([[7., 4.], [-2., 2.]])
		expectedValues = [[-6., -2.], [5., 2.]]
		w = u - v
		self.assertEqual(w.values, expectedValues)
		u -= v
		self.assertEqual(u.values, expectedValues)

	def test_matrix_scl(self):
		u = Matrix([[1., 2.], [3., 4.]])
		expectedValues = [[2., 4.], [6., 8.]]
		v = u * 2
		self.assertEqual(v.values, expectedValues)
		u *= 2
		self.assertEqual(u.values, expectedValues)

	def test_matrix_mul_vector(self):
		u = Matrix.identity(2)
		v = Vector([4., 2.])
		w = u * v
		self.assertEqual(w.values, [4., 2.])

		u = 2 * Matrix.identity(2)
		w = u * v
		self.assertEqual(w.values, [8., 4.])

		u = Matrix([[2., -2.], [-2., 2.]])
		w = u * v
		self.assertEqual(w.values, [4., -4.])

	def test_matrix_mul_matrix(self):
		u = Matrix.identity(2)
		v = u * u
		self.assertEqual(v.values, [[1., 0.], [0., 1.]])

		v = Matrix([[2., 1.], [4., 2.]])
		w = u * v
		self.assertEqual(w.values, [[2., 1.], [4., 2.]])

		u = Matrix([[3., -5.], [6., 8.]])
		w = u * v
		self.assertEqual(w.values, [[-14., -7.], [44., 22.]])

	def test_matrix_trace(self):
		u = Matrix.identity(2)
		self.assertEqual(u.trace(), 2.)

		u = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])
		self.assertEqual(u.trace(), 9.)

		u = Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]])
		self.assertEqual(u.trace(), -21.)

	def test_matrix_transpose(self):
		u = Matrix([[1., 2.], [3., 4.]])
		v = u.transpose()
		self.assertEqual(v.values, [[1., 3.], [2., 4.]])

		u = Matrix([[3., 4., 5.], [6., 7., 8.]])
		v = u.transpose()
		self.assertEqual(v.values, [[3., 6.], [4., 7.], [5., 8.]])

	def test_matrix_row_echelon(self):
		u = Matrix.identity(3)
		v = u.row_echelon()
		self.assertEqual(v.values, u.values)

		u = Matrix([[1., 2.], [3., 4.]])
		v = u.row_echelon()
		self.assertEqual(v.values, [[1., 0.], [0., 1.]])

		u = Matrix([[1., 2.], [2., 4.]])
		v = u.row_echelon()
		self.assertEqual(v.values, [[1., 2.], [0., 0.]])

		u = Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])
		v = u.row_echelon()
		expectedValues = [[1., 0.625, 0., 0., -12.1666667], [0., 0., 1., 0., -3.6666667], [0., 0., 0., 1., 29.5]]
		for i in range(3):
			for j in range(5):
				self.assertAlmostEqual(v.values[i][j], expectedValues[i][j])

	def test_matrix_determinant(self):
		u = Matrix([[1., -1.], [-1., 1.]])
		self.assertEqual(u.determinant(), 0.)

		u = 2 * Matrix.identity(3)
		self.assertEqual(u.determinant(), 8.)

		u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
		self.assertEqual(u.determinant(), -174.)

		u = Matrix([[8., 5., -2., 4.], [4., 2.5, 20., 4.], [8., 5., 1., 4.], [28., -4., 17., 1.]])
		self.assertEqual(u.determinant(), 1032.)

	def test_matrix_inverse(self):
		u = Matrix.identity(3)
		v = u.inverse()
		self.assertEqual(v.values, u.values)

		u *= 2
		v = u.inverse()
		self.assertEqual(v.values, [[0.5, 0., 0.], [0., 0.5, 0.], [0., 0., 0.5]])

		u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
		v = u.inverse()
		expectedValues = [[0.649425287, 0.097701149, -0.655172414], [-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]]
		for i in range(3):
			for j in range(3):
				self.assertAlmostEqual(v.values[i][j], expectedValues[i][j])

		u = Matrix([[-5., 0., 2.], [1., -2., 3.], [6., -2., 1.]])
		with self.assertRaises(ValueError):
			u.inverse()

	def test_matrix_rank(self):
		u = Matrix.identity(3)
		self.assertEqual(u.rank(), 3)

		u = Matrix([[ 1., 2., 0., 0.], [ 2., 4., 0., 0.], [-1., 2., 1., 1.]])
		self.assertEqual(u.rank(), 2)

		u = Matrix([[ 8., 5., -2.], [ 4., 7., 20.], [ 7., 6., 1.], [21., 18., 7.]])
		self.assertEqual(u.rank(), 3)
