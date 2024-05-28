'''
Crie um programa em python que leia o nome de todos os alunos
e depois imprima
'''

alunos = []
while True:
    nome = input('Digite o nome: ')
    if (nome == ''):
        break
    alunos.append(nome)

print(alunos)
for aluno in alunos:
    print(f"Aluno: {aluno}")

