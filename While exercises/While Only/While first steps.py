Selector = str(input('Digite o seu sexo[M/F]: '))
while(Selector != 'MmFf'):
    Selector = str(input('Digite o seu sexo[M/F]: '))
    if(Selector in 'MmFf'):
        print('Nada de errado por aqui!')
        break
