Numbers = (int(input('Type a number: ')), int(input('Type a number: ')), int(input('Type a number: ')), int(input('Type a number: ')))
Counter = 0
print('The sequence was: {}'.format(Numbers))
print('The number 9 in the sequence is shown {} times'.format(Numbers.count(9)))
if(3 in Numbers):
    print('The number 3 is shown in the {} position'.format(Numbers.index(3)+1))
else:
    print('The number 3 is not showed in the sequence')
for i in Numbers:
    if(i % 2 == 0):
        Counter += 1
print('At all {} numbers are even'.format(Counter))
