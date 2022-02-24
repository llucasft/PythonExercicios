from datetime import date
total_menores = 0
total_maiores = 0
ano_atual = date.today().year
for c in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {c}° pessoa: '))
    if ano_atual - nasc < 18:
        total_menores += 1
    else:
        total_maiores += 1
print(f'O total de menores de idade é de {total_menores} pessoas. ')
print(f'O total de maiores de idade é de {total_maiores} pessoas. ')