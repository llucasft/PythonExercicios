# Calculando IMC
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / pow(altura, 2)

if imc < 18.5:
    print(f'IMC atual: {imc:.2f}')
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'IMC atual: {imc:.2f}')
    print('PESO NORMAL')
elif imc >= 25 and imc < 30:
    print(f'IMC atual: {imc:.2f}')
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print(f'IMC atual: {imc:.2f}')
    print('OBESIDADE')
else:
    print(f'IMC atual: {imc:.2f}')
    print('OBESIDADE GRAVE')
