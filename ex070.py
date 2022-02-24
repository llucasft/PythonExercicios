totalgasto = 0
maismil = 0
valorbarato = 0
cont = 0
nomebarato = ''
while True:
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Quanto custa o produto? '))
    totalgasto += preco
    cont += 1
    if preco > 1000:
        maismil += 1
    if cont == 1 or preco < valorbarato:
        valorbarato = preco
        nomebarato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'O total da compra é de R${totalgasto:.2f}')
print(f'{maismil} produtos custaram mais de R$1000.00 ')
print(f'O produto mais barato foi {nomebarato} custando R${valorbarato:.2f}')
