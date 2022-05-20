import random

Counter = 1
GenerateNumber = random.randint(0, 11)
Guess = int(input('Guess a number to compare with the computer: '))
while(Guess != GenerateNumber):
    if(Guess != GenerateNumber):
        print('You failed, try again!')
        GenerateNumber = random.randint(0, 11)
        Guess = int(input('Guess a number to compare with the computer: '))
        Counter += 1
if(Guess == GenerateNumber):
    print('Congrats! you got that! you tried {} times, Good luck next time'.format(Counter))
