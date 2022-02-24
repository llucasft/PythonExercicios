# Pedra papel tesoura
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('PEDRA PAPEL TESOURA')
jogador = int(input('''Digite sua jogada 
[0] PEDRA
[1] PAPEL
[2] TESOURA
'''))

if computador == 0:
    print('Computador jogou PEDRA ')
    if jogador == 0:
        print('''Jogador jogou PEDRA
EMPATE''')
    elif jogador == 1:
        print('''Jogador jogou PAPEL
JOGADOR VENCEU''')
    elif jogador ==2:
        print('''Jogador jogou TESOURA
COMPUTADOR VENCEU''')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    print('Computador jogou PAPEL ')
    if jogador == 0:
        print('''Jogador jogou PEDRA
COMPUTADOR VENCEU''')
    elif jogador == 1:
        print('''Jogador jogou PAPEL
EMPATE''')
    elif jogador == 2:
        print('''Jogador jogou TESOURA
JOGADOR VENCEU ''')
    else:
        print('JOGADA INVÁLIDA ')
elif computador == 2:
    print('Computador jogou TESOURA ')
    if jogador == 0:
        print('''Jogador jogou PEDRA
JOGADOR VENCEU ''')
    elif jogador == 1:
        print('''Jogador jogou PAPEL
COMPUTADOR VENCEU''')
    elif jogador == 2:
        print('''Jogador jogou TESOURA
EMPATE''')
    else:
        print('JOGADA INVÁLIDA ')