n = int(input('Escolha um número inteiro: '))
print('''Escolha uma das bases de conversão:
 [1] converter para BINÁRIO
 [2] converter para OCTAL
 [3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido pra binário é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido pra octal é igual a {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido pra hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente!')