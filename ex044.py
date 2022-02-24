# Gerenciador de pagamentos
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pagamento = int(input('Qual a opção? '))
if pagamento == 1:
    preco = preco - (preco*10/100)
    print(f'Valor total a pagar com 10% de desconto R${preco:.2f}')
elif pagamento == 2:
    preco = preco - (preco*5/100)
    print(f'Valor total a pagar com 5% de desconto R${preco:.2f}')
elif pagamento == 3:
    print(f'Valor total a pagar R${preco:.2f}')
elif pagamento == 4:
    preco = preco + (preco*20/100)
    print(f'Valor total a pagar com 20% de juros {preco:.2f}')
    parcelas = int(input('Em quantas parcelas? '))
    valor_parcelas = preco/parcelas
    print(f'Compra efetuada em {parcelas} parcelas de {valor_parcelas:.2f}')
else:
    print('OPÇÃO INVÁLIDA')