# Radar eletrônico
velocidade = float(input('Qual a velocidade que o carro passou? '))
if velocidade > 80:
    print(f'Velocidade acima do permitido, você foi multado! ')
    valor = (velocidade - 80) * 7
    print(f'O valor da multa a pagar é de R${valor:.2f}')
else:
    print('Tudo certo. ')
