n1 = int(input('Digite o número um'))
n2 = int(input('Digite o número dois'))

if(n1 > n2):
    print('O número {} é maior que o número {}'.format(n1, n2))
elif(n1 < n2):
    print('O número {} é maior que o número {}'. format(n2, n1))
elif(n1 == n2):
    print('Não existe número maior, os dois tem o mesmo valor')
    