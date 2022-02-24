condicao = ''
n = 0
media = 0
total_digitados = 0
maior = 0
menor = 0
total = 0
while condicao != 'N':
    n = int(input('Digite um número: '))
    condicao = str(input('Quer continuar? [S/N] '))
    total_digitados += 1
    total += n
    media = total / total_digitados
    if total_digitados == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'A média entre todos os valores digitados foi de {media:.2f}')
print(f'O maior valor digitado foi {maior}')
print(f'E o menor valor digitado foi {menor}')

