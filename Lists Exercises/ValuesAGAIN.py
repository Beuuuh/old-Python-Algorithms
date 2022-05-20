Biggest = 0
Smallest = 0
Values = []
for i in range(1, 6):
    Values.append(int(input('Type a value: ')))
for t in Values:
    Smallest = t
    if(Biggest < t):
        Biggest = t
    elif(Smallest > t):
        Smallest = t
print('The biggest number: {}'.format(Biggest))
print('The smallest number: {}'.format(Smallest))
print('The biggest number is in the {} position'.format(Values.index(Biggest)+ 1))
print('The smallest number is in the {} position'.format(Values.index(Smallest)+ 1))
