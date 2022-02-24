jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
c = 0

while c < partidas:
    jogador['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
    c += 1

totalgols = sum(jogador['gols'])
jogador['total'] = totalgols
print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}. ')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas. ')

c = 0

for gols in jogador['gols']:
    print(f'{" ":>2} => Na partida {c}, fez {gols} gols. ')
    c += 1

print(f'Foi um total de {totalgols} gols. ')
