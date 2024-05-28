'''
Escreva um algoritmo que leia certa quantidade de 
números e imprima o maior deles e quantas vezes o 
maior numero foi lido. A quantidade de números a 
serem lidos deve ser fornecida pelo usuário.
'''
limite = int(input('Digite ate quantos: '))
maior = 0
qtd_maior = 0
for _ in range(limite):
    numero = int(input('Digite um numero: '))
    if numero > maior:
        maior = numero
        qtd_maior += 1
        
print(f'O maior foi {maior} e digitado {qtd_maior} vezes')
