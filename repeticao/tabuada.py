#tabuada.py
# Crie a tabuada do 9
'''
1 x 9 = 9
2 x 9 = 18
....
10 x 9 = 90
'''
#### Faça as tabuadas do 1 ao 30, com somente mais 2 linhas
for tabuada in range(1, 31):
    for mult in range(1, 11):
        print(f'{mult} x {tabuada} = {mult * tabuada}')
    print("----------------------")