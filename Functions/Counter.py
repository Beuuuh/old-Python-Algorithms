from time import sleep

def Counter(Init, End, Step):
    for f in range(1, 11, 1):
        if(f == 1):
            print("First Count:")
        sleep(0.5)
        print(f, end=' ')
        if(f == 10):
            break
    
    for s in range(10, -1, -2):
        if(s == 10):
            print("\nSecond Count:")
        sleep(0.5)
        print(s, end=' ')
        if(s == 0):
            break

    while(Init != End):
        if(Init > End):
            print(Init, end=' ')
            Init -= Step
            if(Init == End):
                break
        elif(Init < End):
            print(Init, end=' ')
            Init += Step
            if(Init == End):
                break

Start = int(input("Type the start number: "))
TheEnd = int(input("Type the end number: "))
Steped = int(input("Type the step number: "))

Counter(Start, TheEnd, Steped)
