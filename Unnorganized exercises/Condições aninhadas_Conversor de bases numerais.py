numero = int(input('Digite um número para conversão de bases numeráis: '))
selecionador = int(input('Tecle 1 para base de números binários, 2 para octal e 3 para hexadecimal '))

if(selecionador == 1):
    print('O número {} em binário é:'.format(numero) , bin(numero))
elif(selecionador == 2):
    print('O número {} em base octal é:'.format(numero) , oct(numero))
elif(selecionador == 3):
    print('O número {} em binário é:'.format(numero) , hex(numero))
