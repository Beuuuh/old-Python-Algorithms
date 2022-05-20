import math
peso = float(input('Coloque seu peso'))
altura = float(input('Coloque sua altura'))
calculador = float(peso/(altura ** 2))

if(calculador < 18.5):
    print('O seu imc foi: {:.1f} você está com magreza'.format(calculador))
   
if(calculador > 18.5 < 24.9):
    print('O seu imc foi: {:.1f} você está normal!'.format(calculador))

if(calculador > 25.0 < 29.9):
    print('O seu imc foi: {:.1f} você está sobrepeso'.format(calculador))

if(calculador > 30.0 < 39.9):
    print('O seu imc foi: {:.1f} você está com obesidade'.format(calculador))



