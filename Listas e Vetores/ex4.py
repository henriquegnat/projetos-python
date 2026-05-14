lista = []

for i in range(10):
    num = int(input(("Digite um número: ")))
    lista.append(num)


maior = max(lista)
menor = min(lista)

print(f"Maior: {maior}")
print(f"Menor: {menor}")