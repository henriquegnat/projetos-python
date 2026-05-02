quantidade = int(input("Digite a quantidade de alunos na turma: "))
notas = []

for i in range(quantidade):
    nota_aluno = int(input(f"Digite a nota {i + 1}: "))
    notas.append(nota_aluno)

fora_media = 0
media = 0

for nota in notas:
    if nota >= 60:
        media +=1
    else:
        fora_media +=1

print(f"{media} alunos estão na média")

print(f"{fora_media} alunos fora na média")