s = float(input('Qual o salário do funcionário? '))
if s > 1250.00:
    print('O salário com o aumento é de {} reais'.format (s*1.10))
else:
    print('O salário com o aumento é de {} reais'.format (s*1.15))