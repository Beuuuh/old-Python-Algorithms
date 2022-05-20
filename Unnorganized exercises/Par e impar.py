escolha = int(input('Digite um número: '))
poui = escolha % 2

if(poui == 0 ):
    print('O número {} é par'.format(escolha))
else:
    print('O número {} é ímpar'.format(escolha))
