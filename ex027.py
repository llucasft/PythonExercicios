# Primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer! ')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')
