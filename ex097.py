def escreva(mensagem):
    print('-' * (len(mensagem) + 4))
    colocacao = len(mensagem) + 4
    print(f'{mensagem:^{colocacao}}')
    print('-' * (len(mensagem) + 4))


escreva('Olá mundo')
escreva('Curso de Python Funções')
escreva('CEV')

