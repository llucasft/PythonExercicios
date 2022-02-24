def status(year):
    from datetime import datetime
    age = datetime.today().year - year

    if age < 16:
        return f'Com idade {age} não pode votar. '

    elif 16 >= age < 18 or age >= 65:
        return f'Com idade {age} o voto é opcional. '

    else:
        return f'Com idade {age} o voto é obrigatório. '


print('-' * 30)
birth = int(input('Em que ano você nasceu? '))
print(status(birth))
