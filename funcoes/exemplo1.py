def soma():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite um numero: '))
    soma = num1 + num2
    print(f'A soma é: {soma}')


def voltaSoma():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite um numero: '))
    soma = num1 + num2
    return soma


def outraSoma(n1, n2):
    soma = n1 + n2
    return soma


soma()
resultado = voltaSoma()
print(resultado)

resultado2 = outraSoma(3, 3)
print(resultado2)
