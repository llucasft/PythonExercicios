# Aumentos múltiplos
salario = float(input('Qual o seu salário atual? R$ '))
if salario > 1250:
    nsal = salario + (salario * 10 / 100)
    print(f'Você receberá um aumento de 10% e seu novo salário será R${nsal:.2f} ')
else:
    nsal = salario + (salario * 15 / 100)
    print(f'Você receberá um aumento de 15% e seu novo salário será R${nsal:.2f}')
