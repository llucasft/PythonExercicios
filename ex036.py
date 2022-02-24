# Aprovando empréstimo
nome = str(input('Olá, qual o seu nome? '))
valorcasa = float(input('Qual o valor do imóvel? '))
salario = float(input(f'Qual o valor do seu salário, {nome}? '))
parcelas = int(input('Em quantas parcelas deseja pagar o imóvel? '))
# Calculando o valor da prestação.
valorprestacao = valorcasa/parcelas
# Calculando 30% do salário do solicitante.
condition = salario*30/100
if valorprestacao > condition:
    print('Empréstimo negado, o valor da prestação é maior que 30% do seu salário.')
else:
    print('Empréstimo concedido. ')
print(f'O valor das parcelas de um imóvel de R${valorcasa:.0f}, dividido em ', end='')
print(f'{parcelas} parcelas fica no valor de {valorprestacao:.2f} por mês. ')

