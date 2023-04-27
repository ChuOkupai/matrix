from matrix import Complex, Vector, Matrix
import unittest

class TestComplex(unittest.TestCase):
	"""This class contains tests for the Complex class."""

	def test_construct(self):
		c = Complex(1., 2.)
		self.assertEqual(c.r, 1.)
		self.assertEqual(c.i, 2.)
		self.assertEqual(str(c), "(1.0+2.0i)")

	def test_matrix_add(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		v = Matrix([[Complex(9., 10.), Complex(11., 12.)], [Complex(13., 14.), Complex(15., 16.)]])
		expectedValues = [[Complex(10., 12.), Complex(14., 16.)], [Complex(18., 20.), Complex(22., 24.)]]
		w = u + v
		self.assertEqual(w.values, expectedValues)
		u += v
		self.assertEqual(u.values, expectedValues)

	def test_matrix_sub(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		v = Matrix([[Complex(9., 10.), Complex(11., 12.)], [Complex(13., 14.), Complex(15., 16.)]])
		expectedValues = [[Complex(-8., -8.), Complex(-8., -8.)], [Complex(-8., -8.), Complex(-8., -8.)]]
		w = u - v
		self.assertEqual(w.values, expectedValues)
		u -= v
		self.assertEqual(u.values, expectedValues)

	def test_matrix_scl(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		expectedValues = [[Complex(2., 4.), Complex(6., 8.)], [Complex(10., 12.), Complex(14., 16.)]]
		v = u * 2
		self.assertEqual(v.values, expectedValues)
		u *= 2
		self.assertEqual(u.values, expectedValues)

	def test_matrix_mul_vector(self):
		u = Matrix.identity(2)
		v = Vector([Complex(1., 2.), Complex(3., 4.)])
		w = u * v
		self.assertEqual(w.values, [Complex(1., 2.), Complex(3., 4.)])

		u = 2 * Matrix.identity(2)
		w = u * v
		self.assertEqual(w.values, [Complex(2., 4.), Complex(6., 8.)])

		u = Matrix([[2., -2.], [-2., 2.]])
		w = u * v
		self.assertEqual(w.values, [Complex(-4., -4), Complex(4., 4.)])

	def test_matrix_mul_matrix(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		v = Matrix([[Complex(9., 10.), Complex(11., 12.)], [Complex(13., 14.), Complex(15., 16.)]])
		w = u * v
		self.assertEqual(w.values, [[Complex(-28., 122.), Complex(-32., 142.)], [Complex(-36., 306.), Complex(-40., 358.)]])

	def test_matrix_trace(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		self.assertEqual(u.trace(), Complex(8., 10.))

	def test_matrix_transpose(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		v = u.transpose()
		self.assertEqual(v.values, [[Complex(1., 2.), Complex(5., 6.)], [Complex(3., 4.), Complex(7., 8.)]])

	def test_matrix_row_echelon(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)]])
		v = u.row_echelon()
		self.assertEqual(v.values, [[Complex(1., 0.), Complex(2.2, -0.4)]])

	def test_matrix_determinant(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		self.assertEqual(u.determinant(), Complex(0., -16.))

	def test_matrix_inverse(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		v = u.inverse()
		expectedValues = [[Complex(-1/2, 7/16), Complex(1/4, -3/16)], [Complex(3/8, -5/16), Complex(-1/8, 1/16)]]
		for v, e in zip(v.values, expectedValues):
			for x, y in zip(v, e):
				self.assertAlmostEqual(x.r, y.r)
				self.assertAlmostEqual(x.i, y.i)

	def test_matrix_rank(self):
		u = Matrix([[Complex(1., 2.), Complex(3., 4.)], [Complex(5., 6.), Complex(7., 8.)]])
		self.assertEqual(u.rank(), 2)

	def test_vector_add(self):
		u = Vector([Complex(1., -2.), Complex(3., 4.)])
		v = Vector([Complex(5., 6.), Complex(7., 8.)])
		expectedValues = [Complex(6., 4.), Complex(10., 12.)]
		w = u + v
		self.assertEqual(w.values, expectedValues)
		u += v
		self.assertEqual(u.values, expectedValues)

	def test_vector_sub(self):
		u = Vector([Complex(1., -2.), Complex(3., 4.)])
		v = Vector([Complex(5., 6.), Complex(7., 8.)])
		expectedValues = [Complex(-4., -8.), Complex(-4., -4.)]
		w = u - v
		self.assertEqual(w.values, expectedValues)
		u -= v
		self.assertEqual(u.values, expectedValues)

	def test_vector_scl(self):
		u = Vector([Complex(1., -2.), Complex(3., 4.)])
		expectedValues = [Complex(2., -4.), Complex(6., 8.)]
		v = u * 2
		self.assertEqual(v.values, expectedValues)
		u *= 2
		self.assertEqual(u.values, expectedValues)

	def test_vector_dot(self):
		zeros = Vector([Complex(0, 0), Complex(0, 0)])
		ones = Vector([Complex(1, 1), Complex(1, 1)])
		self.assertEqual(zeros.dot(zeros), Complex(0, 0))
		self.assertEqual(zeros.dot(ones), Complex(0, 0))
		self.assertEqual(ones.dot(zeros), Complex(0, 0))
		self.assertEqual(ones.dot(ones), Complex(0, 4))
		u = Vector([Complex(1., 2.), Complex(3., 4.)])
		v = Vector([Complex(5., 6.), Complex(7., 8.)])
		self.assertEqual(u.dot(v), Complex(-18., 68.))
		self.assertEqual(v.dot(u), Complex(-18., 68.))

	def test_vector_norm(self):
		u = Vector([Complex(1., 1.), Complex(2., 2.), Complex(3., 3.)])
		self.assertAlmostEqual(u.norm_1(), 8.48528137)
		self.assertAlmostEqual(u.norm(), 5.29150262)
		self.assertAlmostEqual(u.norm_inf(), 4.24264068)

	def test_vector_angle_cos(self):
		u = Vector([Complex(1., 2.), Complex(3., 4.), Complex(5., 6.)])
		v = Vector([Complex(-1., -2.), Complex(-3., -4.), Complex(-5., -6.)])
		self.assertEqual(u.angle_cos(v), Complex(0.23076923076923078, -0.967032967032967))

	def test_vector_cross_product(self):
		u = Vector([Complex(1., 2.), Complex(3., 4.), Complex(5., 6.)])
		v = Vector([Complex(7., 8.), Complex(9., 10.), Complex(11., 12.)])
		w = u.cross_product(v)
		self.assertEqual(w.values, [Complex(0., -24.), Complex(0., 48.), Complex(0., -24.)])
