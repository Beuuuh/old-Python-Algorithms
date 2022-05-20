import random

numpc = random.randint(1,5)
numpe = int(input('Coloque um número de 1 à 5 e tenha um batalha de advinhação perigosa contra o computador! '))

if(numpe == numpc):
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu! O número era {}'.format(numpc))
