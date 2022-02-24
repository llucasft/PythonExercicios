times = ('Atlético - MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América',
         'Atlético - GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athlético', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport', 'Chapecoense')
print(f'Lista de times do Brasileirão: {times}')
print('-' * 30)
print(f'Os cinco primeiro colocados: {times[0:5]}')
print('-' * 30)
print(f'Os últimos quatro são: {times[16:]}')
print('-' * 30)
print(sorted(times))
print('-' * 30)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')