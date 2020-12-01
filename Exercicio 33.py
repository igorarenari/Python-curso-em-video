x = int(input('Escolha um número: '))
y = int(input('Escolha outro número: '))
z = int(input('Escolha mais um número: '))
menor = x
if y<x and y<z:
    menor = y
if z<x and z<y:
    menor = z
maior = x
if y>x and y>z:
    maior = y
if z>x and z>y:
    maior = z
print('O maior valor é {} e o menor é {}'.format(maior, menor))