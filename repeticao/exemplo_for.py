#exemplo_for.py
# escreva essa frase 50000 vezes
# algoritmos e programacao

limite = 0

while limite <= 100:
    print(f'algoritmos e programacao {limite}')
    limite = limite + 1

print(f'{limite}')

power_ranger_vermelho = [*range(10)]
power_ranger_azul = [*range(7, 77)]
power_ranger_verde = [*range(10, 60, 5)]

print(power_ranger_vermelho)
print(power_ranger_azul)
print(power_ranger_verde)


for n in range(10):
    print(f'n: {n}')
