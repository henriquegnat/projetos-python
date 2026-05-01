import numpy as np

matriz = np.random.randint(1, 100, size=(3, 4))

print("Matriz:")
print(matriz)

maior = matriz.max()

print(f"\nMaior valor: {maior}")