"""
def Sum(a, b, c):
    Adder = (a + b) * c
    print('The sum is {}'.format(Adder))

Sum(80, 900, 1000000)
"""
#Calculator
def Sum(FrstNum, SecNum):
    Adder = FrstNum + SecNum
    print(f"The sum is: {Adder}")

def Minus(FrstNum, SecNum):
    Minor = FrstNum - SecNum
    print(f"The minus is: {Minor}")

def Multiply(FrstNum, SecNum):
    Multipl = FrstNum * SecNum
    print(f"The multiplication is: {Multipl}")

def Division(FrstNum, SecNum):
    Divisor = FrstNum / SecNum
    print(f"The division is: {Divisor}")

Counter = 0
while True:
    Num1 = int(input('Type the first number: '))
    Num2 = int(input('Type the second number: '))
    SelectKey = str(input('[+] [-] [*] [/]'))
    Counter += 1
    if(Counter >= 2):
        StopContinue = str(input('Do you want to stop?[Y/N]: '))
    if(SelectKey == '+'):
        Sum(Num1, Num2)
    elif(SelectKey == '-'):
        Minus(Num1, Num2)
    elif(SelectKey == '*'):
        Multiply(Num1, Num2)
    elif(SelectKey == '/'):
        Division(Num1, Num2)
    else:
        print('You have put something else, please type again')
        SelectKey = str(input('[+] [-] [*] [/]'))
    if(Counter >= 2):
        if(StopContinue in 'Yy'):
            break
