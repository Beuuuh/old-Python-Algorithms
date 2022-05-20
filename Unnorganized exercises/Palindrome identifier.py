Phrase = str(input('Digite uma frase: ')).strip().upper()
Separator = Phrase.split()
Replacer = ''.join(Separator)
Reverse = ''

for l in range(len(Replacer) - 1, -1, -1):
    Reverse += Replacer[l]
if(Reverse == Replacer):
    print('A frase {} de trás pra frente é {}, potanto ela é um palíndromo'.format(Phrase, Reverse))
else:
    print('A frase {} de trás pra frente é {}, portanto ela não é um palíndromo'.format(Phrase, Reverse))
    