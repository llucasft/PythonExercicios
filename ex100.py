from random import randint
from time import sleep


def sorteia():
    numeros = []
    print('Sorteando valores da lista: ', end='')

    while len(numeros) < 5:
        n = randint(1, 10)
        numeros.append(n)

    for numero in numeros:
        print(numero, end=' ')
        sleep(0.5)

    print('PRONTO! ')

    somapar(numeros)


def somapar(lista):
    totalpar = 0
    print(f'Somando os valores pares de {lista} ', end='')

    for numero in lista:
        if numero % 2 == 0:
            totalpar += numero

    print(f'temos {totalpar}')


sorteia()
