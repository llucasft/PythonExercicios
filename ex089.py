tudo = []

while True:

    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    tudo.append([nome, [nota1, nota2], media])
    continua = input('Quer continuar? [S/N] ')

    if continua in 'Nn':

        break

print('-=' * 30)
print('N°  NOME        MÉDIA')
print('-' * 25)

for n, aluno in enumerate(tudo):

    print(f'{n:<4}{aluno[0]:<10}{aluno[2]:>6.1f}')

print('-' * 30)

while True:

    mostrar = int(input('Quer ver as notas de qual aluno? (999 interrompe): '))

    if mostrar == 999:

        break
    else:

        for n, aluno in enumerate(tudo):

            if n == mostrar:

                print(f'Nostas de {aluno[0]} são {aluno[1]}')
                print(' ')
