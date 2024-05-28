#collections/exemplo1.py

lista_pessoa = ['a', 'b', 'c', 'd', 'e']
print(lista_pessoa[4])
print(len(lista_pessoa))

lista_pessoa.append('XXX')
lista_pessoa.remove('b')

for elemento in lista_pessoa:
    print(elemento)
