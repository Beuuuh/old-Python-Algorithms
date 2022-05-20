from math import factorial

Number = int(input('Digite um número: '))
Counter = Number
Factorial = factorial(Number)
while(Counter > 0):
    print('{}'.format(Counter), end='')
    print(' x ' if Counter > 1 else ' = {}'.format(Factorial), end='')
    Counter -= 1
print('O fatorial de {}! é: {}'.format(Number, Factorial))
