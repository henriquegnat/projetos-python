import numpy as np

matriz = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]])

print("Matriz 5x5:")
print(matriz)


diagonal_secundaria = np.fliplr(matriz).diagonal()

print(f"\nDiagonal secundária: {diagonal_secundaria}")