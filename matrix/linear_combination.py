from matrix.vector import Vector

def linear_combination(u: list, coefs: list):
	"""Computes the linear combination of a list of vectors.

	Args:
		u (list): A list of vectors.
		coefs (list): A list of coefficients.

	Returns:
		Vector: The linear combination of the vectors.
	"""
	v = Vector([0] * len(u[0]) if len(u) else [])
	for w, c in zip(u, coefs):
		v += w * c
	return v
