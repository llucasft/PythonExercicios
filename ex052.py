print('Verificador de número primo')
n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
print(f'O número {n} foi divisível {total} vezes')
if total == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')