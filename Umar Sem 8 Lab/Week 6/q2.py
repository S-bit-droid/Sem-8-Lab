import numpy as np
a = np.matrix([
    [2,3,4],
    [5,6,3],
    [1,2,3]
])
b = np.matrix([
    [1,2,3],
    [9,8,7],
    [4,5,6]
])
sum = a + b
mul = a * b
print("Matrix Sum: \n", sum)
print("Matrix Multiplication: \n", mul)