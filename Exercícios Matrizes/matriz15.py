matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matriz original:")
for linha in matriz:
    print(linha)
n = len(matriz)

rotacionada = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotacionada[j][n-1-i] = matriz[i][j]

print("\nMatriz rotacionada 90° (horário):")
for linha in rotacionada:
    print(linha)