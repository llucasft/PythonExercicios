from datetime import datetime

pessoa = dict()
pessoa['nome'] = input('Nome: ')
anonasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - anonasc
pessoa['ctps'] = int(input('Carteira de trabalho (0 Não tem): '))

if pessoa['ctps'] != 0:

    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + 35

    print('-=' * 30)

    for k, v in pessoa.items():

        print(f'{k} tem o valor {v}')

else:

    print('-=' * 30)

    for k, v in pessoa.items():

        print(f'{k} tem o valor {v}')
