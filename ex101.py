from date import datetime


def status():
    birth = int(input('Em que ano você nasceu? '))
    age = date.today().year - birth

    if age < 16:
        return ("Não pode votar. ")

    elif age >= 16 and age < 18 or age >= 70:
        return ("Voto opcional. ")

    else:
        return ("Voto obrigatório. ")


print('-' * 30)
situation = verificarstatus()