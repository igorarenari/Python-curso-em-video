from time import sleep
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-=-'*20)
print('Analisador de triângulos, processando')
print('-=-'*20)
sleep(2)
if r1< r2+r3 and r2< r1+r3 and r3< r1+r2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')