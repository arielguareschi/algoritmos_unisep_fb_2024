n = int(input("digite um numero inteiro: "))

soma = 0

for x in range(1, n):
    if n % x == 0:
        soma += x

print(f"A soma dos valores divisies por{n}:", soma)