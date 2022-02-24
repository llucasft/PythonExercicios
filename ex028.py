# Jogo da adivinhação
from random import randint
from time import sleep
n = int(input('Estou pensando em um número de 0 a 5, que número é esse? '))
certo = randint(0, 5)
print('PROCESSANDO..')
sleep(2)
if n == certo:
    print('Você acertou! ')
else:
    print('Você errou!')
print(f'O número que eu pensei foi {certo}')
