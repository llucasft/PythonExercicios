numeros =  (int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o último número: ')))
nove = 0
for numero in numeros:
    if numero == 9:
        nove += 1
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {nove} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('O número 3 não foi digitado em nenhuma posição ')
print(f'Os valores pares digitados foram ', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')