def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} marcou {gols} gol(s) no campeonato. ')


n = input('Nome do jogador: ')
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
