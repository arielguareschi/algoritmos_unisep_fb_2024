'''
carro.py
Crie uma aplicação Python com o seguinte menu:
1 - Adicionar
2 - Remover
3 - Listar
4 - Verificar se está na lista
0 - Sair
Onde seja possivel adicionar, remover ou listar ou procurar
os carros cadastrados em uma lista.
O usuário irá informar o nome do carro, a placa e o valor.
Não deve deixar cadastrar a placa de um carro que já foi cadastrado 
anteriormente. utilize funções para desenvolver a aplicação.
'''

# list -> []
# tuple ->()
# dict -> {}

carros = {}  # cria o dicionario vazio


def menu():
    print('1 - Adicionar')
    print('2 - Remover')
    print('3 - Listar')
    print('4 - Buscar')
    print('0 - Sair')
    opt = input('Selecione a opção: ')
    return opt


def add():
    placa = input('Informe a placa: ')
    modelo = input('Informe o Modelo: ')
    valor = float(input('Informe o Valor: '))
    carros[placa] = (modelo, valor)


def caminho(opt):
    match opt:
        case '1':
            add()
        case '2':
            remover()
        case '3':
            listar()
        case '4':
            buscar()
        case '0':
            return False
    return True


def main():
    while True:
        opt = menu()
        if not caminho(opt):
            break


if __name__ == '__main__':
    main()
    # carros.pop(placa)
