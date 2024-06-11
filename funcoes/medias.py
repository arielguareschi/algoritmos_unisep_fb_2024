# medias.py
'''
Tera uma lista de alunos, com as notas de b1 e b2,
um menu para selecionar a opcao
1 - adicionar aluno
2 - listar aluno
3 - remover aluno
4 - procurar aluno
5 - aprovados
6 - reprovados
0 - sair
'''
alunos = {}


def menu():
    try:
        print(' 1 - adicionar aluno')
        print(' 2 - listar aluno')
        print(' 3 - remover aluno')
        print(' 4 - procurar aluno')
        print(' 5 - aprovados')
        print(' 6 - reprovados')
        print(' 7 - Procurar pelo nome do aluno')
        print(' 8 - Média da turma B1')
        print(' 9 - Média da turma B2')
        print('10 - Média da turma GERAL')
        print('11 - Diario da turma')
        print(' 0 - sair')
        opt = int(input('Digite a opção: '))
        return opt
    # except KeyboardInterrupt:
    #     print('Deu pau no teclado')
    # except ValueError:
    #     print('Numero digitado errado!')
    except Exception as e:
        print(f'Opção inválida: {e}')
        return 9
    # finally:
    #     print('mostra isso!')


def add_aluno():
    try:
        ra = input('Digite o RA do Aluno: ')
        nome = input('Digite o nome do Aluno: ')
        nota_b1 = float(input('Digite a nota B1 do Aluno: '))
        nota_b2 = float(input('Digite a nota B2 do Aluno: '))
        dados = {"nome": nome, 'b1': nota_b1, 'b2': nota_b2}
        alunos[ra] = dados
    except Exception as e:
        print(f"Alguma coisa digitado errado! {e}")


def listar_alunos():
    for ra, dados in alunos.items():
        aluno = f'RA: {ra} - '
        aluno += f'Nome: {dados['nome']} - '
        aluno += f'B1: {dados['b1']} - '
        aluno += f'B2: {dados['b2']}'
        print(aluno)
    input('Pressione qualquer tecla para continuar')


def remover_aluno():
    ra = input('Digite o RA do Aluno: ')
    if ra in alunos:
        aluno = alunos.pop(ra)
        print(f'O aluno:{aluno['nome']} foi removido')
    else:
        print("Aluno não encontrado!")
    input('Pressione qualquer tecla para continuar')


def procurar_aluno():
    ra = input('Digite o RA do Aluno: ')
    if ra in alunos:
        dados = alunos[ra]
        aluno = f'RA: {ra} - '
        aluno += f'Nome: {dados['nome']} - '
        aluno += f'B1: {dados['b1']} - '
        aluno += f'B2: {dados['b2']}'
        print(aluno)
    else:
        print("Aluno não encontrado!")
    input('Pressione qualquer tecla para continuar')


# Vai listar somente os alunos que a média é maior ou igual a 7
def aprovados():
    for ra, dados in alunos.items():
        if ((dados['b1'] + dados['b2']) / 2) >= 7.0:
            aluno = f'RA: {ra} - '
            aluno += f'Nome: {dados['nome']} - '
            aluno += f'B1: {dados['b1']} - '
            aluno += f'B2: {dados['b2']}'
            print(aluno)
    input('Pressione qualquer tecla para continuar')


# Vai listar somente os alunos que a média é menor a 7
def reprovados():
    for ra, dados in alunos.items():
        if ((dados['b1'] + dados['b2']) / 2) < 7.0:
            aluno = f'RA: {ra} - '
            aluno += f'Nome: {dados['nome']} - '
            aluno += f'B1: {dados['b1']} - '
            aluno += f'B2: {dados['b2']}'
            print(aluno)
    input('Pressione qualquer tecla para continuar')


def buscar_aluno_nome():
    nome = input('Digite o nome do aluno: ')
    nome = nome.upper
    for ra, dados in alunos.items():
        if (dados['nome'].upper == nome):
            aluno = f'ALUNO ENCONTRADO - RA: {ra} - '
            aluno += f'Nome: {dados['nome']} - '
            aluno += f'B1: {dados['b1']} - '
            aluno += f'B2: {dados['b2']}'
            print(aluno)
            break
    input('Pressione qualquer tecla para continuar')


def media_b1():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados['b1']
        qtd += 1
    media = soma / qtd
    print(f'A media de B1 é: {media:.2f}')
    input('Pressione qualquer tecla para continuar')


def media_b2():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados['b2']
        qtd += 1
    media = soma / qtd
    print(f'A media de B2 é: {media:.2f}')
    input('Pressione qualquer tecla para continuar')


def media_geral():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += (dados['b1'] + dados['b2']) / 2
        qtd += 1
    media = soma / qtd
    print(f'A media geral da turma é: {media:.2f}')
    input('Pressione qualquer tecla para continuar')


if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                add_aluno()
            case 2:
                listar_alunos()
            case 3:
                remover_aluno()
            case 4:
                procurar_aluno()
            case 5:
                aprovados()
            case 6:
                reprovados()
            case 7:
                buscar_aluno_nome()
            case 8:
                media_b1()
            case 9:
                media_b2()
            case 10:
                media_geral()
            case 0:
                break
