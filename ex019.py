# Sorteando um item na lista
from random import choice
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno sorteado foi {escolhido}')
