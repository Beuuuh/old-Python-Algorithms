'''
Left = 0
Right = 0
Parentesis = str(input('Type a expression: '))
for i in Parentesis:
    if(i == '('):
        Left += 1
    elif(i == ')'):
        Right += 1
print('The right {}'.format(Right))
print('The left {}'.format(Left))
'''
Expression = str(input('Type a expression: '))
Amount = []
for i in Expression:
    if(i == '('):
        Amount.append('(')
    elif(i == ')'):
        if(len(Amount) > 0):
            Amount.pop()
        else:
            Amount.append(')')
            break
if(len(Amount) == 0):
    print('Your expression is ok')
else:
    print('Your expression is wrong')
