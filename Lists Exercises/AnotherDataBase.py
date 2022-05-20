Values = []
Counter = 0
while True:
    Values.append(int(input('Type a number: ')))
    SelectorKey = str(input('Do you want to stop?[Y/N] '))
    Counter += 1
    if(SelectorKey in 'Yy'):
        print('The amount of numbers are: {}'.format(Counter))
        Values.sort(reverse=True)
        print('The numbers in the data base reversed: {}'.format(Values))
        if(5 in Values):
            print('The number 5 is shown in the {}° position'.format(Values.index(5)+ 1))
        else:
            print('In the data base is no number 5!')
        break
