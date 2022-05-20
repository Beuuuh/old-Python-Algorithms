n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

escolha = input('Coloque a operação selecionada: ')

soma = float(n1 + n2)
sub = float(n1 - n2)
mult = float(n1 * n2)
div = float(n1 / n2)

if(escolha == '+'):
    print('O resultado é de: {}'.format(soma))
if(escolha == '-'):
    print('O resultado é de: {}'.format(sub))
if(escolha == '*'):
    print('O resultado é de: {}'.format(mult))
if(escolha == '/'):
    print('O resultado é de: {}'.format(div))
