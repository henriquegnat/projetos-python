import numpy as np

matriz = np.array([[1, 2, 3],
                   [2, 4, 5],
                   [3, 5, 6]])

print("Matriz:")
print(matriz)

eh_simetrica = np.array_equal(matriz, matriz.T)

print(f"\nÉ simétrica? {eh_simetrica}")