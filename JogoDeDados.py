import random

dado1 = random.randrange(1, 6)
dado2 = random.randrange(1, 6)

print('JOGO DOS DADOS')
print('-' * 35)
start = str(input('DIGITE "JOGAR" PARA COMEÇAR: ')).upper()
if start == 'JOGAR':
    print('-' * 35)
    print(f'dado 1: {dado1}\n dado 2: {dado2}')
else:
    print('-' * 35)
    print('COMANDO INVÁLIDO')
