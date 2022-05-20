Number = int(input('Digite um número '))
counter = 0 

for c in range(1, Number + 1):
    if(Number % c == 0):
        print('\033[34m{}'.format(c, end=' '))
        counter += 1
    else:
        print('\033[31m{}'.format(c, end=' '))

if(counter > 2):        
    print('\nO número {} foi divisivel {} vezes, portanto, ele NÃO é um número primo'.format(Number, counter))
else:
    print('\nO número {} foi dividido apenas por um e por ele mesmo, portanto, ele É um número primo'.format(Number, counter))
