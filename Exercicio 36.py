c = float(input('Qual o valor da casa?'))
s = float(input('Qual o seu salário?'))
t = int(input('Em quantos meses você quer pagar?'))
if c/(s*t)>1.7:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi permitido')
    print('O valor da parcela é: {}'.format(c/t))