lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continua = input('Quer continuar? [S/N] ')
    if continua in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {lista} ')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
