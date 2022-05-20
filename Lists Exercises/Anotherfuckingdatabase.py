ValuesGeneral = []
EvenValues = []
OddValues = []
while True:
    Number = int(input('Type a value: '))
    ValuesGeneral.append(Number)
    SelectorKey = str(input('Do you want to stop?[Y/N] '))
    if(Number % 2 == 0):
        EvenValues.append(Number)
    elif(Number % 2 == 1):
        OddValues.append(Number)
    if(SelectorKey in 'Yy'):
        print('-----------------------------------------------------')
        break
print('All numbers: {}'.format(ValuesGeneral))
print('The even numbers are: {}'.format(EvenValues))
print('All the odd numbers are: {}'.format(OddValues))
