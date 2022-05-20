Number = int(input('Type a number to show his times table [Type a negative number to stop the program]'))
Ten = 0
while True:
    while(Ten != 10 and Number > 0):
        Ten += 1
        Multiply = Number * Ten
        print('{} x {} = {}'.format(Number, Ten, Multiply))
        if(Ten == 10):
            Number = int(input('Type a number to show his times table [Type a negative number to stop the program]'))
            Ten = 0
    if(Number < 0):
        break
