termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo}')
        termo += razao
        c += 1
    mais = int(input('Quer mostrar mais quantos termos? '))
