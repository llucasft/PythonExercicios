jogador = dict()
todos = list()
while True:

    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    c = 0

    while c < partidas:

        jogador['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
        c += 1

    totalgols = sum(jogador['gols'])
    jogador['total'] = totalgols
    todos.append(jogador.copy())
    continua = input('Quer continuar? [S/N] ')

    if continua in 'Nn':
        break
print(todos)
print('-=' * 30)
print(f'cod nome {" ":>4} gols {" ":>4} total')
print('-' * 30)

cod = 0

for jogador in todos:

    print(f'{cod} {jogador["nome"]} {jogador["gols"]} {jogador["total"]} ')
    cod += 1
print('-' * 30)

while True:
    escolha = int(input('Mostrar dados de qual jogador? '))

    if escolha == 999:
        break

    elif escolha > len(todos):
        print(f'Erro, jogador {escolha} não existe')

    else:
        levantamento = todos[escolha]
        print(f'LEVANTAMENTO DO JOGADOR {levantamento["nome"]}')

        c = 0

        for gols in levantamento['gols']:

            print(f'{" ":>2} => Na partida {c}, fez {gols} gols. ')
            c += 1

print('<< VOLTE SEMPRE >>')
