from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR! ')
ganhador = ''
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Você quer PAR ou ÍPAR? [P/I] ')).strip().upper()[0]
    soma = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}, resultado {soma} ')
    print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            vitorias += 1
            print('VOCÊ GANHOU')
        else:
            print('VOCÊ PERDEU ')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            vitorias += 1
            print('VOCÊ GANHOU ')
        else:
            print('VOCÊ PERDEU')
            break
print(f'GAME OVER! Você venceu {vitorias} vezes. ')
