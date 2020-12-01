from random import randint
from time import sleep
computador = randint(0, 5) #FAZ O COMPUTADOR ESCOLHER UM NUMERO ALEATORIO ENTRE 0 E 5
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5')
print('-=-' *20)
jogador = int(input('Em que número pensei?'))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você me venceu!')
else:
    print('Ganhei, eu pensei no número {}, não no número {}'.format(computador, jogador))