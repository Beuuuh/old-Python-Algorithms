Grade1 = float(input('Insira sua nota da prova parcial: '))
Grade2 = float(input('Insira sua nota de trabalho: '))
Grade3 = float(input('Insira sua nota da prova global: '))
Calculator = (Grade1 + Grade2 + Grade3)/3
RecNotes = [5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9]

if(Calculator <= 5.0):
    print('Você está de reprovado!')
elif(Calculator in RecNotes):
    print('Você está de recuperação')
elif(Calculator >= 7.0):
    print('Você foi aprovado!')
