from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
total = 1
quantidade = int(input('Quantos jogos você quer sortear? '))
while total <= quantidade:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('=-=-=-=-= < BOA SORTE! > =-=-=-=-=')