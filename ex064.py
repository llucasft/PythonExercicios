total_numeros = 0
soma_total = 0
n = 0
while n != 999:
    n = int(input('Digite um número (999 PARA SAIR): '))
    if n != 999:
        total_numeros += 1
        soma_total += n
print(f'Ao todo você digitou {total_numeros}, e a soma entre eles é {soma_total}')
