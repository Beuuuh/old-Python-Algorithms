nome = str(input('Digite seu nome'))
divididado = (nome.split())

print('Seu nome com todas as letras maiúsculas:' , nome.upper())

print('Seu nome com todas as letras minúsculas:' , nome.lower())

print('Ao todo seu nome tem:' , len(nome) - nome.count(' ') , 'letras')

print('E seu primeiro nome tem:' , len(divididado[0]) , 'letras')
