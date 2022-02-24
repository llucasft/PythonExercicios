# Conversor de bases numéricas
n = int(input('Digite um número: '))
print('BASE DE CONVERSÃO')
print('Digite [1] para binário')
print('Digite [2] para octal')
print('Digite [3] para hexadecimal')
escolha = int(input('Digite aqui -> '))
if escolha == 1:
    print(f'O número {n} em binário é {bin(n)[2:]}')
elif escolha == 2:
    print(f'O número {n} em octal é {oct(n)[2:]}')
elif escolha == 3:
    print(f'O número {n} em hexadecimal é {hex(n)[2:]}')
else:
    print('ERRO NÚMERO INVÁLIDO')
