import random
from typing import Counter

PorI = int(input('Type a number: '))
Decision = str(input('Even or odd? [E/O]: '))
PcNumber = random.randint(1,10)
Sum = PcNumber  + PorI
Counter = 0

while True:
    if(Sum % 2 == 1 and Decision == 'O'):
        print('You win!')
        PorI = int(input('Type a number: '))
        Decision = str(input('Even or odd? [E/O]: '))
        Counter += 1
    elif(Sum % 2 == 0 and Decision == 'E'):
        print('You win!')
        PorI = int(input('Type a number: '))
        Decision = str(input('Even or odd? [E/O]: '))
        Counter += 1
    else:
        break
print('You lose :c At least you won {} games!'.format(Counter))
