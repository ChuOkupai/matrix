from copy import deepcopy
from matrix.complex import Complex
from matrix.vector import Vector
import math

def is_close(x, y, abs_tol=1e-9):
	"""Returns whether two numbers are close enough to be considered equal."""
	if isinstance(x, Complex):
		return abs(x - y) < abs_tol
	return math.isclose(x, y, abs_tol=abs_tol)

class InvalidShapeError(ValueError):
	def __init__(self, msg="Invalid shape"):
		super().__init__(msg)

class NotSquareError(ValueError):
	def __init__(self, msg="Matrix is not square"):
		super().__init__(msg)

class Matrix:
	pass

class Matrix:
	"""This class represents a matrix."""

	@staticmethod
	def identity(n: int, dtype=float):
		"""Returns an identity matrix.

		Args:
			n (int): The size of the matrix.
			dtype (type, optional): The type of the matrix. Defaults to float.

		Returns:
			Matrix: An identity matrix.
		"""
		return Matrix([[dtype(i == j) for j in range(n)] for i in range(n)])

	def __init__(self, values: list):
		"""Initializes a matrix.

		Args:
			values (list): A list of values.

		Raises:
			InvalidShapeError: If the matrix is not rectangular.
			TypeError: If values is not a list of dtype.
		"""
		if values is None:
			values = []
		if (any(len(x) == 0 for x in values) or
			any(len(x) != len(values[0]) for x in values)):
			raise InvalidShapeError
		if len(values):
			if (any(not isinstance(x, list) for x in values) or
				any(any(not isinstance(y, type(values[0][0])) for y in x) for x in values)):
				raise TypeError(f"values must be a 2d list of {type(values[0][0])}")
			self.shape = (len(values), len(values[0]))
		else:
			self.shape = (0, 0)
		self.values = values

	def _assert_same_shape(self, other):
		"""Asserts that the matrices have the same shape.

		Args:
			other (Matrix): The other matrix.

		Raises:
			InvalidShapeError: If the matrices do not have the same shape.
		"""
		if self.shape != other.shape:
			raise InvalidShapeError("Matrices must have the same shape")

	def _assert_square(self):
		"""Asserts that the matrix is square.

		Raises:
			NotSquareError: If the matrix is not square.
		"""
		if not self.is_square():
			raise NotSquareError

	def _det2x2(self, i: int, cols: list):
		"""Returns the determinant of a 2x2 submatrix."""
		m = self.values
		return m[i][cols[0]] * m[i + 1][cols[1]] - m[i][cols[1]] * m[i + 1][cols[0]]

	def _det3x3(self, i: int, cols: list):
		"""Returns the determinant of a 3x3 submatrix."""
		m = self.values
		return (m[i][cols[0]] * self._det2x2(i + 1, cols[1:]) -
				m[i][cols[1]] * self._det2x2(i + 1, [cols[0]] + cols[2:]) +
				m[i][cols[2]] * self._det2x2(i + 1, cols[:2]))

	def _do_op_matrix(self, other, op):
		self._assert_same_shape(other)
		return Matrix([[op(x, y) for x, y in zip(r1, r2)] for r1, r2 in zip(self.values, other.values)])

	def _rref(self):
		"""Transforms the matrix into reduced row echelon form."""
		m = self.values
		for i in range(self.rows()):
			for j in range(self.cols()):
				if ((isinstance(m[i][j], (float, int)) and m[i][j] != 0)
					or (isinstance(m[i][j], Complex) and m[i][j].r != 0)):
					m[i] = [x / m[i][j] for x in m[i]]
					for k in range(self.rows()):
						if k != i:
							m[k] = [x - y * m[k][j] for x, y in zip(m[k], m[i])]
					break

	def cols(self):
		"""Returns the number of columns."""
		return self.shape[1]

	def rows(self):
		"""Returns the number of rows."""
		return self.shape[0]

	def is_close(self, other: Matrix, delta=1e-9):
		"""Returns whether the matrix is close to another matrix.

		Args:
			other (Matrix): The other matrix.
			delta (float, optional): The maximum difference between the values.

		Returns:
			bool: Whether the matrix is close to another matrix.
		"""
		if self.shape != other.shape:
			return False
		return all(all(is_close(x, y, abs_tol=delta) for x, y in zip(r1, r2)) for r1, r2 in zip(self.values, other.values))

	def is_square(self):
		"""Returns whether the matrix is square or not."""
		return self.cols() == self.rows()

	def trace(self):
		"""Computes the trace of the matrix.

		Returns:
			float: The trace of the matrix.

		Raises:
			NotSquareError: If the matrix is not square.
		"""
		self._assert_square()
		return sum(self.values[i][i] for i in range(self.rows()))

	def transpose(self):
		"""Returns the transpose of the matrix."""
		return Matrix([[self.values[j][i] for j in range(self.rows())] for i in range(self.cols())])

	def row_echelon(self):
		"""Returns the row echelon form of the matrix."""
		m = deepcopy(self)
		m._rref()
		return m

	def determinant(self):
		"""Computes the determinant of the matrix.

		Returns:
			float: The determinant of the matrix.

		Raises:
			NotSquareError: If the matrix is not square.
		"""
		self._assert_square()
		if self.rows() > 4:
			raise ValueError("Matrix must be 4x4 or smaller")
		if self.rows() == 1:
			return self.values[0][0]
		if self.rows() == 2:
			return self._det2x2(0, [0, 1])
		if self.rows() == 3:
			return self._det3x3(0, [0, 1, 2])
		cols = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
		return sum((-1) ** i * self.values[0][i] * self._det3x3(1, cols[i]) for i in range(4))

	def inverse(self):
		"""Computes the inverse of the matrix.

		Returns:
			Matrix: The inverse of the matrix.

		Raises:
			NotSquareError: If the matrix is not square.
			ValueError: If the matrix is not invertible.
		"""
		self._assert_square()
		a2 = deepcopy(self)
		dtype = type(self.values[0][0]) if self.cols() > 0 else float
		id = Matrix.identity(self.rows(), dtype=dtype)
		for i in range(a2.rows()):
			a2.values[i] += id.values[i]
		a2.shape = (a2.rows(), 2 * a2.cols())
		a2._rref()
		for i in range(a2.rows()):
			a2.values[i] = a2.values[i][a2.cols() // 2:]
		a2.shape = (a2.rows(), a2.cols() // 2)
		id2 = self * a2
		if id2.is_close(id):
			return a2
		raise ValueError("Matrix is not invertible")

	def rank(self):
		"""Computes the rank of the matrix.

		Returns:
			int: The rank of the matrix.
		"""
		m = self.row_echelon()
		return sum(any(x != 0 for x in r) for r in m.values)

	def __add__(self, other):
		if isinstance(other, Matrix):
			return self._do_op_matrix(other, lambda x, y: x + y)
		raise NotImplementedError

	def __iadd__(self, other):
		if isinstance(other, Matrix):
			self._assert_same_shape(other)
			for i in range(self.rows()):
				for j in range(self.cols()):
					self.values[i][j] += other.values[i][j]
			return self
		raise NotImplementedError

	def __imul__(self, other):
		if isinstance(other, (float, int)):
			for i in range(self.rows()):
				for j in range(self.cols()):
					self.values[i][j] *= other
			return self
		if isinstance(other, Matrix):
			self._assert_same_shape(other)
			for i in range(self.rows()):
				for j in range(self.cols()):
					self.values[i][j] *= other.values[i][j]
			return self
		if isinstance(other, Vector):
			if self.cols() != len(other):
				raise InvalidShapeError("Vector must have length equal to number of columns")
			return Vector([sum(x * y for x, y in zip(r, other.values)) for r in self.values])
		raise NotImplementedError

	def __isub__(self, other):
		if isinstance(other, Matrix):
			self._assert_same_shape(other)
			for i in range(self.rows()):
				for j in range(self.cols()):
					self.values[i][j] -= other.values[i][j]
			return self
		raise NotImplementedError

	def __mul__(self, other):
		if isinstance(other, (float, int)):
			return Matrix([[x * other for x in r] for r in self.values])
		if isinstance(other, Matrix):
			if self.cols() != other.rows():
				raise InvalidShapeError("Number of columns in first matrix must equal number of rows in second matrix")
			return Matrix([[sum(x * y for x, y in zip(r1, r2)) for r2 in zip(*other.values)] for r1 in self.values])
		if isinstance(other, Vector):
			if self.cols() != len(other):
				raise InvalidShapeError("Vector must have length equal to number of columns")
			return Vector([sum(x * y for x, y in zip(r, other.values)) for r in self.values])
		raise NotImplementedError

	def __radd__(self, other):
		return self + other

	def __rmul__(self, other):
		return self * other

	def __sub__(self, other):
		if isinstance(other, Matrix):
			return self._do_op_matrix(other, lambda x, y: x - y)
		raise NotImplementedError

	def __repr__(self):
		return f"Matrix({self.values})"

	def __str__(self):
		return str(self.values)
