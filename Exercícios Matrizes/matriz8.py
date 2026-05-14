import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matriz:")
print(matriz)

medias = matriz.mean(axis=1)

print("\nMédia de cada linha:")
for i, media in enumerate(medias):
    print(f"Linha {i}: {media}")