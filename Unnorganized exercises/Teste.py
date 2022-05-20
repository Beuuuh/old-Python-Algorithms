import math
import random
coiso = str(input('digite algo: '))
coiso1 = str(input('digite outro algo: '))
coiso2 = str(input('digite mais um algo: '))
coiso3 = str(input('digite o último algo: '))
lista = [coiso, coiso1, coiso2, coiso3]
random.shuffle(lista)

print(lista)
