from time import sleep
ano = int(input('Diga um ano para ver se ele é bissexto: '))
resultado = ano %4
print('PROCESSANDO...')
sleep(2)
if resultado == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))