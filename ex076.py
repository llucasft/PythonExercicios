produtos = ('Carne', 45.5,
            'Arroz', 25.75,
            'Feijão', 20,
            'Açafrão', 5.99,
            'Molho', 12.75,
            'Alho', 5,
            'Macarrão', 13.25,
            'Farinha', 7.15,
            'Óleo', 3,
            'Margarina', 8.20)
print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)
