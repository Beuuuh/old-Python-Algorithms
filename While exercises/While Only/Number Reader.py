Number = int(input('Type a number [Or 0 for exit the program]: '))
Counter = 0
Sum = Number
BiggestNumber = Number
SmallestNumber = Number
while(Number != 0):
    Number = int(input('Type a number [Or 0 for exit the program]: '))
    if(Number != 0):
        Sum = Number + Number
    Counter += 1
    if(BiggestNumber < Number):
        BiggestNumber = Number
    if(SmallestNumber > Number):
        if(Number != 0):
            SmallestNumber = Number
if(Counter != 0):
    Media = Sum/Counter
    print('The media is: {}, the biggest and the smallest number typed, respectivly is {} and {}'.format(Media, BiggestNumber, SmallestNumber))
else:
    print('Goodbye!')
