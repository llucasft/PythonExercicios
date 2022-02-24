# Jogo da adivinhação
from random import randint
jogador = 11
tentativas = 0
computador = randint(0, 10)
print('Estou pensando em um número de 0 a 10, consegue adivinhar qual é? ')
while jogador != computador:
    jogador = int(input('Adivinhe o número de 0 a 10: '))
    tentativas += 1

print(f'ACERTOU, o número correto é {computador}!')
print(f'Você precisou de {tentativas} tentativas para acertar! ')