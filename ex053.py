frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
if frase == frase[::-1].strip():
    print(f'A frase {frase} é um palíndromo! ')
    print(f'''Frase {frase} de trás para frente 
é igual: {frase[::-1]}''')
else:
    print(f'A frase {frase} não é um palíndromo! ')
    print(f'''Frase {frase} de trás para frente
não é igual: {frase[::-1]}''')
