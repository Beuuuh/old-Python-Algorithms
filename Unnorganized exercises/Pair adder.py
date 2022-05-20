Sum = Count = 0
for c in range(1, 7):
    Number = int(input('Digite o {} número '.format(c)))
    if(c % 2 == 0):
        Sum += c
        Count += 1
print('Você digitou {} números pares, a soma deles vale {}'.format(Count, Sum))
