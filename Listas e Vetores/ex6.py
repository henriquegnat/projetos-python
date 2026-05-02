pares = []
impar = []
for i in range(5):
    num = int(input("Digite um número: "))

    if num %2 == 0:
        pares.append(num)
    elif num %2 == 1:
        impar.append(num)

if pares:
    maior_par = max(pares)
    print(f"\nO maior par é {maior_par}")

    soma_par = sum(pares)
    print("A soma dos números pares é", soma_par)

    leitura_par = len(pares)

    media_pares = (soma_par/leitura_par)
    print("A média dos números pares", media_pares)

else:
    print("Não foram inseridos números pares")

if impar:
    menor_impar = min(impar)
    print(f"\nO menor numero ímpar é {menor_impar}")

    soma_impar = sum(impar)
    print("A soma dos números ímpares é", soma_impar)

    leitura_impar = len(impar)

    media_impares = (soma_impar / leitura_impar)
    print("A média dos números ímpares", media_impares)
else:
    print("Não foram inseridos números ímpares")
