def lerp(u, v, t: float):
	"""Computes the linear combination of two objects.

	Args:
		u: The first object.
		v: The second object.
		t (float): The interpolation coefficient.

	Returns:
		An object resulting from the linear interpolation.

	Raises:
		TypeError: If u and v are not of the same type.
	"""
	if type(u) != type(v):
		raise TypeError("u and v must be of the same type")
	return u + t * (v - u)
