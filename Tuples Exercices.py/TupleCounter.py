Selector = int(input('Type a number between 1 and 20: '))
Estented = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', '60', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fiveteen', 'Sixteen', 'Seventeen', 'Eighteen', 'NineTeen', 'Twenty')
while True:
    if(Selector >= 1 and Selector <= 20):
        print('You put the {} number'.format(Estented[Selector - 1]))
        break
    else:
        print('You have put something else, try again')
        Selector = int(input('Type a number between 1 and 20: '))
