# Classificando atletas
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
anoatual = date.strftime("%Y")
anoatual = int(anoatual)

print(anoatual)

anonasc = int(input('Qual seu ano de nascimento? '))
idade = anoatual - anonasc

if idade <= 9:
    print('Sua categoria é MIRIM ')
elif idade <= 14:
    print('Sua categoria é INFANTIL ')
elif idade <= 19:
    print('Sua categoria é JUNIOR ')
elif idade <= 20:
    print('Sua categoria é SENIOR ')
elif idade > 20:
    print('Sua cateoria é MASTER ')