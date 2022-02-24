# Alistamento militar
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = year - nasc
if idade < 18:
    print('Fique atento, logo precisará se alistar. ')
elif idade > 18:
    atraso = idade - 18
    print(f'Você já deveria ter se alistado há {atraso} anos')
elif idade == 18:
    print('Está na hora de se alistar. ')
