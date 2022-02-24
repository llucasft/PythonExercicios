# Custo da viagem
distancia = float(input('Qual a distância do destino em KM? '))
if distancia <= 200:
    valor = 0.50 * distancia
else:
    valor = 0.45 * distancia
print(f'O valor da passagem é R${valor:.2f}')
