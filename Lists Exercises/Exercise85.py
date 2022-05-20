Value = 0
AllValues = [[], []]
for i in range(1, 8):
    Value = int(input('Type the {}° number'.format(i)))
    if(Value % 2 == 0):
        AllValues[0].insert(Value)
    else:
        AllValues[1].insert(Value)
AllValues[0].sort()
AllValues[1].sort()
print('The evens {}'.format(AllValues[0]))
print('The odds {}'.format(AllValues[1]))
