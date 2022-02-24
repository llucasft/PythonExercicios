# Validação de dados
sexo = str(input('Informe seu sexo: [M/F] '))
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: [M/F] '))
print(f'Sexo {sexo} cadastrado com sucesso, obrigado! ')
