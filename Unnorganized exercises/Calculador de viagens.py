kilometragem = int(input('Qual a distância da cidade? '))
money = kilometragem * 0.50
Money = kilometragem * 0.70

if(kilometragem > 200):
    print('O valor da passagem vai ser: {}'.format(Money))
else:
    print('O valor da passagem vai ser: {}'.format(money))
    