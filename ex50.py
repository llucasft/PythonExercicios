soma_pares = 0
total_pares = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}o número: '))
    if n % 2 == 0:
        soma_pares += n
        total_pares += 1
print(f'Você digitou {total_pares} números pares e a soma entre eles é {soma_pares}')
