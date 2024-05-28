n = 4000000
ultimo = 0
penultimo = 0
soma = 0

while ultimo <= n:
    if ultimo % 2 == 0:
        soma += ultimo
    print(ultimo)
    ultimo = ultimo + penultimo
    penultimo = ultimo - penultimo
    if ultimo == 0:
        ultimo = ultimo + 1
        
print(soma)
