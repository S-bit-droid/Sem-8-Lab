import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", a)

matrix_2x3 = a.reshape(2, 3)
print("2x3 Matrix:\n", matrix_2x3)

matrix_3x2 = a.reshape(3, 2)
print("\n3x2 Matrix:\n", matrix_3x2)