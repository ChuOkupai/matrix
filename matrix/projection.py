from math import radians, tan
from matrix.matrix import Matrix

def projection(fov: float, ratio: float, near: float, far: float):
	"""Returns a projection matrix for the given parameters.

	Args:
		fov (float): The field of view in degrees.
		ratio (float): The aspect ratio of the rendering window.
		near (float): The distance to the near plane.
		far (float): The distance to the far plane.
	"""
	fov = radians(fov)
	f = 1. / tan(fov / 2.)
	return Matrix([
		[f / ratio, 0., 0., 0.],
		[0., f, 0., 0.],
		[0., 0., (far + near) / (near - far), (2. * far * near) / (near - far)],
		[0., 0., -1., 0.]
	])
