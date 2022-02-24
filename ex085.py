todos = [[], []]
for c in range(1, 8):

    n = int(input(f'Digite o {c}° valor: '))

    if n % 2 == 0:
        todos[0].append(n)
        todos[0].sort()

    else:
        todos[1].append(n)
        todos[1].sort()


print('-=' * 30)
print(f'Os valores pares digitados foram: {todos[0]}')
print(f'Os valores ímpares digitados foram: {todos[1]}')
print(todos)

