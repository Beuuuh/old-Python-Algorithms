Counter = int(input('Type a number: '))
First = 0
Second = 1
Timer = 2
print('{} -> {} '.format(First, Second), end='')
while(Timer != Counter):
    Result = First + Second
    print('-> {} '.format(Result), end='')
    First = Second
    Second = Result
    Timer += 1
print('The end')
