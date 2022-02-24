valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'nN':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} valores. ')
valores.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são {valores}')
if 5 in valores:
    print('O número 5 está na lista! ')
else:
    print('Não encontrei o número 5 na lista! ')
