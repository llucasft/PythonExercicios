while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(n, ' x ', c, ' = ', n*c)

print('PROGRAMA ENCERRADO, VOLTE SEMPRE! ')