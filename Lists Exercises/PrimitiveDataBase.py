Values = []
SelectorKey = ''
while True:
    Values.append(int(input('Type a number to guard it in a data base: ')))
    SelectorKey = str(input('Do you want to stop?[Y/N] '))
    if(SelectorKey in 'Yy'):
        print('All the numbers is in this sequence: {}'.format(Values))
        Values.sort()
        print('The numbers in order sequence: {}'.format(Values))
        break
    else:
        continue
