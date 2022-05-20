Age = int(input('Digite sua idade: '))

if(Age <= 9):
    print('Mirim')
elif(Age <= 14 ):
    print('Infantil')
elif(Age <= 19):
    print('Junior')
elif(Age == 20):
    print('Sênior')
elif(Age > 20):
    print('Master')

#Modo antigo{
#Age = int(input('Digite sua idade: '))
#Childhood = [10,11,12,13,14]
#Junior = [15,16,17,18,19]

#if(Age <= 9):
#    print('Mirim')
#elif(Age in Childhood):
#    print('Infantil')
#elif(Age in Junior):
#    print('Junior')
#elif(Age == 20):
#    print('Sênior')
#elif(Age > 20):
#    print('Master')
#}