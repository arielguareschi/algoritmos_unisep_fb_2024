'''
arquivo: par_impar.py
Solicite para o usuario informar um numero e quais ele quer 
exibir, (par ou impar).
Exiba todos os numeros do INTERVALO informado, mostrando
quais são pares ou impares conforme a escolha.
'''

limite = int(input('Informe ate qual numero: '))
opcao = input('Pares ou Impares? (P - I) ')

for num in range(1, limite + 1):
    if num % 2 == 0:
        if opcao.upper() == 'P':
            print(f'O numero {num} eh par!')
    else:
        if opcao.upper() == 'I':
            print(f'O numero {num} eh impare!')
