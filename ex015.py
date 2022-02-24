# Aluguel de carros
# Custo da diária 60 reais por dia
# Custo KM rodados 0.15 centavos por KM

qtdias = int(input('Quantos dias ficou alugado? '))
qtkm = float(input('Quantos KM foram rodados? '))
pdias = 60*qtdias
pkm = 0.15 * qtkm
ptotal = pdias + pkm
print(f'Valor total a pagar: R${ptotal:.2f} ')

from math import sqrt