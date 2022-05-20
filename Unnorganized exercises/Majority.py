Major = 0
Minor = 0
for p in range(1, 7):
    BirthDay = int(input('Digite o ano do seu nascimento: '))
    Age = 2021 - BirthDay
    if(Age >= 18 ):
        Major += 1
    else:
        Minor += 1
print('A pesquisa apontou que {} pessoas são maiores de idade e {} são menores de idade'.format(Major, Minor))
