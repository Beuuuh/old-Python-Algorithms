FirstNumber = float(input('Type the first number: '))
SecondNumber =  float(input('Type the second number: '))
Selection = int(input('What do you want to do with them?\n[1] for sum they\n[2] to multiply they\n[3] to compare they\n[4] to put other numbers\n[5] to turn off the program\n'))
while(Selection != 5):
    if(Selection == 1):
        Sum = FirstNumber + SecondNumber
        print('The sum of the numbers ({}) + ({}) was: {}'.format(FirstNumber, SecondNumber, Sum))
        Selection = int(input('What do you want to do with them?\n[1] for sum they\n[2] to multiply they\n[3] to compare they\n[4] to put other numbers\n[5] to turn off the program\n'))
    elif(Selection == 2):
        Multiply = FirstNumber * SecondNumber
        print('The multiplication of the numbers ({}) * ({}) was: {}'.format(FirstNumber, SecondNumber, Multiply))
        Selection = int(input('What do you want to do with them?\n[1] for sum they\n[2] to multiply they\n[3] to compare they\n[4] to put other numbers\n[5] to turn off the program\n'))
    elif(Selection == 3):
        if(FirstNumber > SecondNumber):
            print('The first number ({}) its bigger than the second number ({})'.format(FirstNumber, SecondNumber))
            Selection = int(input('What do you want to do with them?\n[1] for sum they\n[2] to multiply they\n[3] to compare they\n[4] to put other numbers\n[5] to turn off the program\n'))
        elif(SecondNumber > FirstNumber):
            print('The second number ({}) its bigger than the first number ({})'.format(SecondNumber, FirstNumber))
            Selection = int(input('What do you want to do with them?\n[1] for sum they\n[2] to multiply they\n[3] to compare they\n[4] to put other numbers\n[5] to turn off the program\n'))
    elif(Selection == 4):
        FirstNumber = float(input('Type the first number: '))
        SecondNumber =  float(input('Type the second number: '))
        Selection = int(input('What do you want to do with they?\n[1] for sum they\n[2] to multiply they\n[3] to compare they\n[4] to put other numbers\n[5] to turn off the program\n'))
