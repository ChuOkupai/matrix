from matrix import projection
import os

if __name__ == '__main__':
	if len(os.sys.argv) != 5:
		print('Usage: python3 projection.py fov ratio near far')
		print('Example: python3 projection.py 90 1.7777 0.5 100')
		exit(1)
	try:
		fov, ratio, near, far = map(float, os.sys.argv[1:])
	except ValueError:
		print('Error: fov, ratio, near, and far must be numbers', file=os.sys.stderr)
		exit(1)
	p = projection(fov, ratio, near, far)
	for row in p.values:
		print(', '.join(map(str, row)))
