Temporary = []
Main = []
Heavyest = Light = 0
while True:
    Temporary.append(str(input('Type your name: ')))
    Temporary.append(str(input('Type your weight: ')))
    if(len(Main) == 0):
        Heavyest = Light = Temporary[1]
    else:
        if(Temporary[1] > Heavyest):
            Heavyest = Temporary[1]
        elif(Temporary[1] < Light):
            Light = Temporary[1]
    Main.append(Temporary[:])
    Temporary.clear()
    SelectKey = str(input('Do you want to stop?[Y/N] '))
    if(SelectKey in 'Yy'):
        break
print('-=' * 30, end='-')
print('\nAmount {}'.format(len(Main)))
print('The biggest number {}, the heaviest ones '.format(Heavyest, end=''))
for p in Main:
    if(p[1] == Heavyest):
        print('{}'.format(p[0], end=' '))
print('\nThe lowest number {}, the light ones '.format(Light, end=''))
for p in Main:
    if(p[1] == Light):
        print('The lighest ones: {}'.format(p[0], end=' '))
