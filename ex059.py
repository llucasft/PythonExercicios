# Menu de opções
opcao = 0
while opcao != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print(f'O que deseja fazer com {n1} e {n2}? ')
    opcao = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
OPÇÃO -> '''))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'O produto entre {n1} e {n2} é {n1 * n2}')
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior valor entre os dois é {maior} ')
    elif opcao == 4:
        print('VOLTANDO..')
    else:
        print('OPÇÃO INVÁLIDA. ')
