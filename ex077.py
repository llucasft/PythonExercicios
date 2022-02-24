palavras = ('cadeado', 'grande', 'pequeno', 'ilha', 'viagem', 'trabalho', 'amigos', 'felicidade')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')