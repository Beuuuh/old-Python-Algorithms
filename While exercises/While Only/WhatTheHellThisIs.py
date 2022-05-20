Number = int(input('Type a number (if you dont want to, just type 999) '))
Sum = Number
while(Number != 999):
    Number = int(input('Type a number (if you dont want to, just type 999) '))
    if(Number != 999):
        Sum = Sum + Number
print('A soma foi {}'.format(Sum))
