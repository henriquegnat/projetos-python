import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matriz:")
print(matriz)

soma_colunas = matriz.sum(axis=0)

print(f"\nSoma de cada coluna: {soma_colunas}")