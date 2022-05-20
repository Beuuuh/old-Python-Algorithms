print('--Atenção foto sensor a frente--')

carro = int(input('Qual a sua velocidade no momento? '))
multa = int(7)

if(carro > 60):
    carro = carro - 60
    multa = carro * multa
    print('Você ultrapassou 60 Km/H, sua multa é de {} reais'.format(multa))
else:
    print('Tudo dentro dos conformes!')