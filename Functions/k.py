from time import sleep

def contador(i, p, f):
    sleep(0.5)
    print(30 * "-=")
    sleep(0.5)
    if p == 0:
        if i < f:
            print(f"Contagem de {i} até {f} de 1 em 1:")
            for c in range(i, f, p+1):
                sleep(0.5)
                print(c, end=' ')
            print("FIM!")
        if p == 0 and i > f:
            print(f"Contagem de {i} até {f} de 1 em 1:")
            for c in range(i, f, p-1):
                sleep(0.5)
                print(c, end=' ')
            print("FIM!")
    else:
        if i < f:
            print(f"Contagem de {i} até {f} de {p} em {p}:")
            for c in range(i, f, p):
                sleep(0.5)
                print(c, end=" ")
            print("FIM!")
        if i > f and p < 0:
            print(f"Contagem de {i} até {f} de {p * -1} em {p * -1}:")
            for c in range(i, f, p):
                sleep(0.5)
                print(c, end=" ")
            print("FIM!")
        elif i > f:
            print(f"Contagem de {i} até {f} de {p} em {p}:")
            for c in range(i, f, -p):
                sleep(0.5)
                print(c, end=" ")
            print("FIM!")


sleep(0.5)
print(30 * "=-")
sleep(0.5)
print("Contagem de 0 até 10 de 1 em 1:")
for c in range(0, 11, 1):
    sleep(0.5)
    print(c, end=' ')
print("FIM!")
sleep(0.5)
print(40 * "=-")
sleep(0.5)
print("Contagem de 10 até 0 de 2 em 2:")
for c in range(10, -2, -2):
    sleep(0.5)
    print(c, end=' ')
print("FIM!")
sleep(0.5)
print(30 * "=-")
sleep(0.5)
print("Agora é sua vez de personalizar a sua contagem: ")
sleep(0.5)
contador(i=int(input("Início: ")), f=int(input("Fim: ")), p=int(input("Passo: ")))