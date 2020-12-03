d = int(input('Qual a sua data de nascimento? '))
i = 2020 - d
print('Quem nasceu em {} tem {} anos'.format(d, i))
if i == 18:
    print('Você deve se alistar imediatamente!')
elif i > 18:
    print('Já se passaram {} anos do seu alistamento'.format(i-18))
elif i < 18:
    print('Você deve se alistar em {} anos'.format(18-i))