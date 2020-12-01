v = int(input('Qual era a velocidade do carro em km/h?'))
if v>80:
    print('Você foi mutado, sua multa custará {} reais'.format((v-80)*7))
else:
    print('Parabéns, você respeitou os limites de velocidade e poderá seguir sem pagar nada.')