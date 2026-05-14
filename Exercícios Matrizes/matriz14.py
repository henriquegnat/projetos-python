import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Matriz A (2x3):")
print(A)

print("\nMatriz B (3x2):")
print(B)

resultado = A @ B

print("\nA * B (2x2):")
print(resultado)