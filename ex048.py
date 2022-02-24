# Criar um intervalo entre 1 e 500
# Pegar todos ímpares
# Pegar todos os números que são ímpares e múltiplos de 3
total = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        total += c
print(f'A soma entre todos {contador} os números ímpares de 1 até 500 que são múltiplos de 3 é: {total}')
