shopping = float(input('Shopping price: '))
print('''===> FORMAS DE PAGAMENTO <===
[1] à vista dinheiro/pix (10% de desconto)
[2] à vista cartão (5% de desconto)
[3] 2x no cartão
[4] 3x ou mais no cartão (20% de juros)
''')
option = int(input('Escolha a opção: '))
if(option == 1):
    print('R$', shopping - (shopping * 0.1))
elif(option == 2):
    print('R$', shopping - (shopping * 0.05))
elif(option == 3):
    print('R$', shopping)
elif(option == 4):
    print('R$', (shopping * 0.2) - shopping)
else:
    print('[ERROR] Enter a valid number')
