quantidade = int(input("Digite a quantidade de alunos na turma: "))

lista_nomes = []

for i in range(quantidade):
    nome_aluno = input("Digite o nome do aluno: ")
    lista_nomes.append(nome_aluno)

leitura = len(lista_nomes)

print(f"Tem {leitura} alunos na turma")

for aluno in lista_nomes:
    print(aluno)