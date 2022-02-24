# Ano bissexto
from datetime import date
print('VERIFICADOR DE ANO BISSEXTO')
ano = int(input('Digite o ano que quer verificar: (digite 0 para o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto ')
else:
    print(f'O ano {ano} não é um ano bissexto ')
