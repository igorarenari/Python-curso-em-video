n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m < 5.0:
    print('Você está de reprovado!')
elif m >= 7:
    print('Parabéns, você está aprovado!')
else:
    print('Você está de recuperação, estude um pouco mais!')