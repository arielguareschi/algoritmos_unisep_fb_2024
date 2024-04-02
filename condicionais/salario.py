# salario.py
"""
    Quero verificar em qual faixa de contribuicao do inss 
    o salario informado se enquadra.
    de     0,00 até 1.412,00 -  7,5%
    de 1.412,01 até 2.666,68 -  9,0%
    de 2.666,69 até 4.000,03 - 12,0%
    de 4.000,04 até 7.786,02 - 14,0%
    acima de 7.786,03        - R$ 908,85 
"""
"""
salario = 2000.00

if salario <= 1412.00:
    aliquota = 7.5
else:
    if salario >= 1412.01 and salario <= 2666.68:
        aliquota = 9
    else:
        if salario >= 2666.69 and salario <= 4000.03:
            aliquota = 12
        else:
            if salario >= 4000.04 and salario <= 7786.02:
                aliquota = 14
            else:
                valor = 908.65 

print('O salario e....')
"""

nome = input('Digite o nome do escravo: ')
salario = float(input('Digite o salario bruto: '))

if salario <= 1421.00:
    aliquota = 7.5
elif salario >= 1412.01 and salario <= 2666.68:
    aliquota = 9
elif salario >= 2666.69 and salario <= 4000.03:
    aliquota = 12
elif salario >= 4000.04 and salario <= 7786.02:
    aliquota = 14
else:
    valor = 908.85
    
# if salario >= 7786.03: # forma 1
# if valor > 0.0: # forma 2
# if aliquota == 0: # forma 3

if aliquota != 0:
    # salario ---- 100%
    # valor   ---- aliquota
    valor = salario * aliquota / 100

texto = f"""
O salario do funcionario {nome} é: R$ {salario:.2f}
ele está na aliquota de {aliquota:.2f}%
Deve pagar de inss o valor de R$ {valor:.2f}
Recebera o valor de R$ {(salario - valor):.2f}
"""
print(texto)