# 🔢 Matrix

This project is part of 42 school curriculum.
The main goal is to implement mathematical operations on vectors and matrices from scratch.
I've chosen Python as programming language for this project because of its flexibility and simplicity.

## ✨ Features
### ➡️ Basic features

- Object-oriented design
- Support for arbitrary dimensions with generic types
- Provides mathematical operations support such as addition, subtraction and multiplication

### ➡️ Vector-specific features

- Numpy-like ones and zeros functions to create vectors of ones and zeros
- Cosine similarity calculation
- Cross product calculation for 3-dimensional vectors
- Dot product calculation
- Norm calculation (L1, L2, and L-infinity norms)
- Linear combination calculation
- Linear interpolation calculation

### ➡️ Matrix-specific features

- Numpy-like identity function to create identity matrices
- Transposition
- Rank calculation
- Trace calculation
- Determinant calculation for matrices up to 3x3
- Reduced row echelon form calculation (RREF)
- Inverse calculation

### 🎁 Bonus features

These features were not required to validate the mandatory part of the project but I've implemented them anyway because I thought it would be interesting.

- Projection matrix calculation for 3D graphics
- Complex number support (but please don't use it for anything serious 🤡)

## 📦 Prerequisites

You will need to have Python 3 installed on your machine to use it.
I've used Python 3.9.2 to write and test this code but it should most likely work with any version of Python 3.

## 🚀 Usage

Here is a simple example of how to use the matrix in your own code:

```python
from matrix import Matrix

# Create a 3x3 matrix
m1 = Matrix([[1., 2., -1.], [2., 1., 2.], [-1., 2., 1.]])
print("m1 =", m1)

# Calculate the determinant of the matrix
det = m1.determinant()
print("det(m1) =", det)

# Calculate the inverse of the matrix
m1_inv = m1.inverse()
print("m1_inv =", m1_inv)

# Calculate m1 * m2
m3 = m1 * m1_inv
print("m1 * m1_inv =", m3)
```

### 📽️ Matrix projection calculation

Here is an example of how to use the matrix projection calculation:

```sh
python3 projection.py 90 1.7777 0.5 100
```

In order to vizualize the result, you can use the following commands:

```sh
cd matrix_display
python3 ../projection.py 90 1.7777 0.5 100 > proj
./display
cd ..
```

## 🧪 Testing

The source code is covered by unit tests written using the [unittest](https://docs.python.org/3/library/unittest.html) framework provided by Python.
There are located in the [test](matrix/test) directory.

To run the unit tests, you can use the following command:

```sh
python3 -m unittest
```

## ⚖️ License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
