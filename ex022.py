# Analisador de textos
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas {nome.upper()}')
print(f'Seu nome em minúsculas {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome.replace(" ", ""))} letras ')
print(f'Seu primeiro nome tem {nome.find(" ")} letras ')
