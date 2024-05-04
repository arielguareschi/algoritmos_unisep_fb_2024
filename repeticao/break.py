#break.py
for n in range(500):
    if n == 50:
        break
    print(f'N: {n}')
    
        # o break quebra o laco e bota um fim em tudo!

for n in range(10):
    if n % 3 == 0:
        continue
        # pula a rodada da vez no loop e vai para a proxima
    print(f'N: {n}')

while True:	
    opcao = input('Digite X para sair: ')
    print(opcao)
    if opcao.upper() == 'X':
        break

