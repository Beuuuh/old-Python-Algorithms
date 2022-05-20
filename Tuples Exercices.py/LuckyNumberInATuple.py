import random

Guard = random.randint(1, 50)
BiggestNumber = 0
SmallestNumber = Guard
for i in range(1, 5):
    Guard = (random.randint(1, 50))
    if(BiggestNumber < Guard):
        BiggestNumber = Guard
    elif(SmallestNumber > Guard):
        SmallestNumber = Guard
    print(Guard, end=' ')
print('\nThis is the biggest number: {}'.format(BiggestNumber))
print('\nThis is the smallest number: {}'.format(SmallestNumber))
