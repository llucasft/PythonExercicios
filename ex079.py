valores = []
while True:
    entrada = int(input('Digite um valor: '))
    if entrada in valores:
        print('Número duplicado, não vou adicionar. ')
    else:
        valores.append(entrada)
        print('Valor adicionado com sucesso. ')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
