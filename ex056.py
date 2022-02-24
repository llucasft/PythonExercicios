media_idades = 0
total_idades = 0
homem_maior = ''
idade_maior = 0
mulher_menor = ''
total_m_menor_vinte = 0
for c in range(1, 5):
    print(f'{c}ª PESSOA')
    nome = str(input('Digite o nome: ')).strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    total_idades += idade
    # Pegar o nome do homem mais velho
    if sexo == 'M' and idade > idade_maior:
        homem_maior = nome
        idade_maior = idade
    if sexo == 'F' and idade < 20:
        total_m_menor_vinte += 1

media_idades = total_idades/4
print(f'A média de idade entre as 4 pessoas é de {media_idades:.0f} anos. ')
print(f'O nome do homem mais velho é {homem_maior}.')
print(f'E apareceram {total_m_menor_vinte} mulheres com menos de 20 anos. ')
