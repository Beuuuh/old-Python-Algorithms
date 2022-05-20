Values = []
for i in range(0, 5):
    n = int(input('Type a number: '))
    if(i == 0 or n > Values[-1]):
        Values.append(n)
    else:
        Tester = 0
        while(Tester < len(Values)):
            if(n <= Values[Tester]):
                Values.insert(Tester, n)
                break
            Tester += 1
print(Values)
