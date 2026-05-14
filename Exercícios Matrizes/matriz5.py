import numpy as np

print("Preencha a matriz 3x3:")
valores = []

for i in range(9):
    numero = float(input(f"Digite o {i+1}° valor da matriz: "))
    valores.append(numero)

matriz = np.array(valores).reshape(3,3)

print(f"\nMatriz Original: \n{matriz}")

escalar = float(input("\nDigite um número para multiplicar a matriz: "))

print(f"Matriz dps da multiplicação: \n{escalar*matriz}")