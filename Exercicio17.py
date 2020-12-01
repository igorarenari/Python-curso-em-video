import math
c1 = int(input('Cateto oposto: '))
c2 = int(input('Cateto adjacente: '))
h = math.hypot(c1, c2)
print('A hipotenusa é: {}'.format(h))