Year = int(input('Digite o ano do seu nascimento '))
Surgery = str(input('Tem algum tipo de cirurgia ou deficiência, responder SIM ou NÃO '))
YearCalculator = 2021 - Year

if(Surgery == 'NÃO' and YearCalculator == 18):
    print('Já está apto para alistamento.')
elif(YearCalculator < 18):
    print('Ainda não está apto para alistamento.')
elif(YearCalculator > 18):
    print('O alistamento não é mais necessário')

if(Surgery == 'SIM'):
    print('O alistamento não é necessário.')
