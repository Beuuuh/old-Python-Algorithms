A1 = int(input('Digite o primeiro termo (a1) '))
Ratio = int(input('Digite a razão da progressão aritmética (r) '))
An = A1 + (10 - 1) * Ratio
Cont = 0

for n in range(A1, An + Ratio, Ratio):
    Cont += 1
    print(n, end=' ')
