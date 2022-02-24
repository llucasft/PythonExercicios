from time import sleep


def contador(i, f, p):
    print('=-' * 30)

    if p == 0:
        p = 1

    if p < 0:
        p *= -1

    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}: ')

        while i <= f:
            print(i, end=' ')
            sleep(0.5)
            i += p
        print('FIM! ')

    else:
        print(f'Contagem de {i} até {f} de {p} em {p}: ')

        while i >= f:
            print(i, end=' ')
            sleep(0.5)
            i -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 30)
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
