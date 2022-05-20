Matrix = []
for i in range(1, 10):
    Value = int(input('Type a value: '))
    Matrix.append(Value)
for e in Matrix:
    EvenAcumulator = e
    if(e % 2 == 0):
        EvenAcumulator += e
    Third = e[2] + e[5] + e[8]
    if(e[3] > e[4] and e[3] > e[5]):
        Biggest = e[3]
    elif(e[4] > e[5] and e[4] > e[3]):
        Biggest = e[4]
    elif(e[5] > e[4] and e[5] > e[3]):
        Biggest = e[5]
print('-=' * 30, end='-')
print(f'[ {Matrix[0]} ] [ {Matrix[1]} ] [ {Matrix[2]} ]')
print(f'[ {Matrix[3]} ] [ {Matrix[4]} ] [ {Matrix[5]} ]')
print(f'[ {Matrix[6]} ] [ {Matrix[7]} ] [ {Matrix[8]} ]')
print('The biggest number in the 2nd row: {}'.format(Biggest))
print('The 3rd collumn added is: {}'.format(Third))
print('The even numbers was sum, there is the result: {}'.format(EvenAcumulator))
