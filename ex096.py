def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é {a:.1f}m². ')


print('Controle de terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
