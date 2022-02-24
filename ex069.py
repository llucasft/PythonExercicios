sexo = ''
continuar = ''
maior = 0
homens = 0
mulheres = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'Mm':
        homens += 1
    elif sexo in 'Ff' and idade > 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'Ao todo foram cadastrados {homens} homens. ')
print(f'Ao todo foram cadastradas {maior} pessoas com mais de 18 anos. ')
print(f'Ao todo foram cadastradas {mulheres} mulheres com mais de 20 anos. ')
