LowerThan20 = 19
OlderMan = ''
FemaleCounter = 0
AgeAdder = 0
NewerMan = 0
for i in range(1, 5):
    print('-----{} PESSOA-----'.format(i))
    Age = int(input('Put your age: '))
    Name = str(input('Put your name: '))
    Sex = str(input('Put your sex: '))
    AgeAdder += Age
    Media = AgeAdder/i
    if(i == 1):
        Older = Age
        Newer = Age
    elif(Age > Older and Sex == 'Masculino'):
        Older = Age
        OlderMan = Name
    elif(Newer < Age):
        Newer = Age
        NewerMan = Name
    if(Sex == 'Feminino' and Age <= 19):
        FemaleCounter += 1
print(OlderMan)
print(FemaleCounter)
print(Media)
