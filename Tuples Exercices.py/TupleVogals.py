Words = ('Djonga', 'Jojo', 'Celular', 'Cuzcuz', 'Tupla', 'Iridio')
for i in Words:
    print('\nThe word {} has:'.format(i), end=' ')
    for letters in i:
        if(letters.lower() in 'aeiou'):
            print(letters, end=' ')
