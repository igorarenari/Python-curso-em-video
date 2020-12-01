d = float(input('Quantos km é a viagem? '))
if d<=200:
    print('Sua viagem custará {} reais'.format(d*0.5))
else:
    print('Sua viagem custará {} reais'.format(d*0.45))