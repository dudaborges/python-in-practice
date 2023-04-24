# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Enter a integer number: '))
print('''Choose one of the conversion bases:
[1] Binary
[2] Octal
[3] Hexadecimal
''')
option = int(input('Your option: '))
if(option == 1):
    print('The converted number is {}'.format(bin(num)[2:]))
elif(option == 2):
    print('The converted number is {}'.format(oct(num)[2:]))
elif(option == 3):
    print('The converted number is {}'.format(hex(num)[2:]))
