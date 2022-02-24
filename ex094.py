tudo = list()
pessoa = dict()
mulheres = list()
acimamedia = list()

while True:

    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ')

    if pessoa['sexo'] not in 'mfMF':
        print('Erro, valores válidos apenas M ou F. ')

        while pessoa['sexo'] not in 'mMFf':
            pessoa['sexo'] = input('Sexo [M/F]: ')

            if pessoa['sexo'] not in 'mMFf':
                print('Erro, valores válidos apenas M ou F. ')

    pessoa['idade'] = int(input('Idade: '))
    tudo.append(pessoa.copy())
    continua = input('Quer continuar? [S/N] ')

    if continua not in 'SsNn':

        while continua not in 'SsnN':
            print('Erro, digite apenas S ou N! ')
            continua = input('Quer continuar? [S/N] ')

    if continua in 'Nn':
        break

print('-=' * 30)
print(f' - O grupo tem {len(tudo)} pessoas. ')

totalidade = 0

for individuo in tudo:
    totalidade += individuo['idade']

media = totalidade / len(tudo)

print(f' - A média de idade é de {media:.2f} anos. ')

for individuo in tudo:

    if individuo['sexo'] in 'fF':

        mulheres.append(individuo['nome'])

print(f' - As mulheres cadastradas foram: {mulheres}')

for individuo in tudo:

    if individuo['idade'] > media:

        acimamedia.append(individuo.copy())

print(f' - Lista de pessoas que estão acima da média: ')

for dicionario in acimamedia:

    for k, v in dicionario.items():

        print(f'{k} = {v}; ', end='')
    print()
print('<<ENCERRADO>>')