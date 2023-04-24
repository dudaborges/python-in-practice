homeValue = float(input('Valor da casa: R$'))
salary = float(input('Salário do comprador: R$'))
finYears = int(input('Quantos anos de financiamento? '))
instMonth = round((homeValue / finYears) / 12, 2)
print('Para pagar uma casa de R${} em {} anos a prestação será de R${}'.format(homeValue, finYears, instMonth))
if((salary * 0.3) <= instMonth):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo aceito!')