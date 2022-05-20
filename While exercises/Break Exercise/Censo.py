Counter = 0
AgeCounter = 0
MaleCounter = 0
FemaleCounter = 0
while True:
    Counter += 1
    print('----------{} People----------'.format(Counter))
    Sex = str(input('Type your sex [M/F]: '))
    Age = int(input('Type your age: '))
    if(Age > 18):
        AgeCounter += 1
    if(Sex in 'Mm'):
        MaleCounter += 1
    if(Age < 20 and Sex in 'Ff'):
        FemaleCounter += 1
    if(Counter > 1):
        YesOrNo = str(input('Do you want to keep going? [Y/N]: '))
        if(YesOrNo in 'Nn'):
            break
        else:
            Counter += 1
            print('----------{} People----------'.format(Counter))
            Sex = str(input('Type your sex [M/F]: '))
            Age = int(input('Type your age: '))
            YesOrNo = str(input('Do you want to keep going? [Y/N]: '))
            if(YesOrNo in 'Nn'):
                break
print('At all {} people is older than 18 years old'.format(AgeCounter))
print('At all {} people is male'.format(MaleCounter))
print('At all {} women is under 20 years old'.format(FemaleCounter))
