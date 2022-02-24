matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = terceriacoluna = maior = 0

for l in range(0, 3):

    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 3):

    for c in range(0, 3):

        print(f' [{matriz[l][c]:^5}] ', end='')

        if matriz[l][c] % 2 == 0:

            totpar += matriz[l][c]

    print()

print('-=' * 30)
print(f'A soma de todos os números pares da matriz é {totpar} ')

for l in range(0, 3):

    terceriacoluna += matriz[l][2]

print(f'A soma dos valores da terceira coluna é {terceriacoluna}')

for c in range(0, 3):

    if c == 0:
        maior = matriz[1][c]

    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior valor da segunda linha é {maior}')
