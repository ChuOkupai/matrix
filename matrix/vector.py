from math import sqrt

class InvalidLengthError(ValueError):
	def __init__(self, msg="Invalid length"):
		super().__init__(msg)

class Vector:
	pass

class Vector:
	"""This class represents a vector."""

	@staticmethod
	def ones(n: int, dtype=float):
		"""Returns a vector of ones.

		Args:
			n (int): The size of the vector.
			dtype (type, optional): The type of the vector. Defaults to float.

		Returns:
			Vector: A vector of ones.
		"""
		return Vector([dtype(1) for _ in range(n)])

	@staticmethod
	def zeros(n: int, dtype=float):
		"""Returns a vector of zeros.

		Args:
			n (int): The size of the vector.
			dtype (type, optional): The type of the vector. Defaults to float.

		Returns:
			Vector: A vector of zeros.
		"""
		return Vector([dtype(0) for _ in range(n)])

	def __init__(self, values: list):
		"""Initializes a vector.

		Args:
			values (list): A list of values.

		Raises:
			TypeError: All values are not of the same type.
		"""
		if values is None:
			values= []
		if len(values) and any(not isinstance(x, type(values[0])) for x in values):
			raise TypeError(f"values must be a list of {type(values[0])}")
		self.values = values

	def _assert_same_length(self, other):
		"""Asserts that the vectors have the same length.

		Args:
			other (Vector): The other vector.

		Raises:
			InvalidLengthError: If the vectors do not have the same length.
		"""
		if len(self) != len(other):
			raise InvalidLengthError("Vectors must have the same length")

	def _do_op_vector(self, other, op):
		self._assert_same_length(other)
		return Vector([op(x, y) for x, y in zip(self.values, other.values)])

	def angle_cos(self, v: Vector):
		"""Computes the angle between two vectors in radians.

		Args:
			v (Vector): The other vector.

		Returns:
			float: The angle between the two vectors in radians.
		"""
		return self.dot(v) / (self.norm() * v.norm())

	def cross_product(self, v: Vector):
		"""Computes the cross product of two vectors of size 3.

		Args:
			v (Vector): The other vector.

		Returns:
			Vector: The cross product of the two vectors.

		Raises:
			InvalidLengthError: If the vectors do not have the same length.
			ValueError: If the vectors are not of size 3.
		"""
		self._assert_same_length(v)
		if len(self) != 3:
			raise ValueError("Cross product is only defined for 3D vectors")
		v1, v2 = self.values, v.values
		return Vector([
			v1[1] * v2[2] - v1[2] * v2[1],
			v1[2] * v2[0] - v1[0] * v2[2],
			v1[0] * v2[1] - v1[1] * v2[0]
		])

	def dot(self, v: Vector):
		"""Computes the dot product of two vectors.

		Args:
			v (Vector): The other vector.

		Returns:
			float: The dot product of the two vectors.

		Raises:
			InvalidLengthError: If the vectors do not have the same length.
		"""
		self._assert_same_length(v)
		return sum([x * y for x, y in zip(self.values, v.values)])

	def norm_1(self):
		"""Computes the 1-norm of the vector (Manhattan norm).

		Returns:
			float: The 1-norm of the vector.
		"""
		return sum([abs(x) for x in self.values])

	def norm(self):
		"""Computes the 2-norm of the vector (Euclidean norm).

		Returns:
			float: The euclidean norm of the vector.
		"""
		return sqrt(sum([abs(x) ** 2 for x in self.values]))

	def norm_inf(self):
		"""Computes the infinity norm of the vector.

		Returns:
			float: The infinity norm of the vector.
		"""
		return max([abs(x) for x in self.values])

	def __add__(self, other):
		if isinstance(other, Vector):
			return self._do_op_vector(other, lambda x, y: x + y)
		raise NotImplementedError

	def __iadd__(self, other):
		if isinstance(other, Vector):
			self._assert_same_length(other)
			for i in range(len(self)):
				self.values[i] += other.values[i]
			return self
		raise NotImplementedError

	def __imul__(self, other):
		if isinstance(other, (float, int)):
			for i in range(len(self)):
				self.values[i] *= other
			return self
		raise NotImplementedError

	def __isub__(self, other):
		if isinstance(other, Vector):
			self._assert_same_length(other)
			for i in range(len(self)):
				self.values[i] -= other.values[i]
			return self
		return self

	def __mul__(self, other):
		if isinstance(other, (float, int)):
			return Vector([x * other for x in self.values])
		return NotImplementedError

	def __radd__(self, other):
		return self + other

	def __rmul__(self, other):
		return self * other

	def __sub__(self, other):
		if isinstance(other, Vector):
			return self._do_op_vector(other, lambda x, y: x - y)
		return NotImplementedError

	def __len__(self):
		return len(self.values)

	def __repr__(self):
		return f"Vector({self.values})"

	def __str__(self):
		return str(self.values)
