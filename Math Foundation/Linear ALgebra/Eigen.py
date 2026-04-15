import numpy as np
#Define a constant 3x3 matrix
# (symmetric , for real eigenvalues)
A = np.array([[4, 2, 2],
              [2, 3, 1],
              [2, 1, 3]])
# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
#print the results
print("Matrix A:\n", A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
"""
Matrix A:
 [[4 2 2]
 [2 3 1]
 [2 1 3]]
Eigenvalues: [6.82842712 1.17157288 2.        ]
Eigenvectors:
 [[ 7.07106781e-01  7.07106781e-01 -3.14018492e-16]
 [ 5.00000000e-01 -5.00000000e-01 -7.07106781e-01]
 [ 5.00000000e-01 -5.00000000e-01  7.07106781e-01]]
"""