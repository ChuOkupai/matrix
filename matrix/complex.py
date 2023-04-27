from math import sqrt

class Complex:
	pass

class Complex:
	"""Represents a complex number."""

	def __init__(self, real=0.0, imag=0.0):
		self.r = real
		self.i = imag

	def _do_op(self, c, op):
		if isinstance(c, Complex):
			self.r = op(self.r, c.r)
			self.i = op(self.i, c.i)
		else:
			self.r = op(self.r, c)
			self.i = op(self.i, c)
		return self

	def _do_op_with_copy(self, c, op):
		if isinstance(c, Complex):
			return Complex(op(self.r, c.r), op(self.i, c.i))
		return Complex(op(self.r, c), op(self.i, c))

	def __add__(self, c):
		return self._do_op_with_copy(c, lambda x, y: x + y)

	def __iadd__(self, c):
		return self._do_op(c, lambda x, y: x + y)

	def __imul__(self, c):
		if isinstance(c, Complex):
			a, b, c, d = self.r, self.i, c.r, c.i
			self.r = a * c - b * d
			self.i = a * d + b * c
			return self
		return self._do_op(c, lambda x, y: x * y)

	def __isub__(self, c):
		return self._do_op(c, lambda x, y: x - y)

	def __mul__(self, c):
		if isinstance(c, Complex):
			a, b, c, d = self.r, self.i, c.r, c.i
			return Complex(a * c - b * d, a * d + b * c)
		return self._do_op_with_copy(c, lambda x, y: x * y)

	def __radd__(self, c):
		return self._do_op_with_copy(c, lambda x, y: x + y)

	def __rmul__(self, c):
		return self._do_op_with_copy(c, lambda x, y: x * y)

	def __rsub__(self, c):
		return self._do_op_with_copy(c, lambda x, y: x - y)

	def __rtruediv__(self, c):
		if isinstance(c, Complex):
			a, b, c, d = c.r, c.i, self.r, self.i
			c2d2 = c ** 2 + d ** 2
			return Complex((a * c + b * d) / c2d2, (b * c - a * d) / c2d2)
		return self._do_op_with_copy(c, lambda x, y: x / y)

	def __sub__(self, c):
		return self._do_op_with_copy(c, lambda x, y: x - y)

	def __truediv__(self, c):
		if isinstance(c, Complex):
			a, b, c, d = self.r, self.i, c.r, c.i
			c2d2 = c ** 2 + d ** 2
			return Complex((a * c + b * d) / c2d2, (b * c - a * d) / c2d2)
		return self._do_op_with_copy(c, lambda x, y: x / y)

	def __abs__(self):
		return sqrt(self.r ** 2 + self.i ** 2)

	def __pow__(self, c):
		if isinstance(c, Complex):
			a, b, c, d = self.r, self.i, c.r, c.i
			theta = atan2(b, a)
			r = sqrt(a ** 2 + b ** 2)
			return Complex(r ** c * cos(c * theta), r ** c * sin(c * theta))
		return self._do_op_with_copy(c, lambda x, y: x ** y)

	def __eq__(self, o):
		if isinstance(o, Complex):
			return self.r == o.r and self.i == o.i
		return False

	def __ne__(self, o):
		return not (self == o)

	def __repr__(self):
		return f"Complex({self.r}, {self.i})"

	def __str__(self):
		return f"({self.r}{'+' if self.i >= 0 else '-'}{abs(self.i)}i)"
