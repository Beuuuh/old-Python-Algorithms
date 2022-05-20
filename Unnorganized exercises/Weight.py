HigherWeight = 0
LowerWeight = 0

for p in range(1, 6):
    Weight = float(input('{} pessoa, coloque seu peso:'.format(p)))
    if(p == 1):
        HigherWeight = Weight
        LowerWeight = Weight
    elif(Weight > HigherWeight):
        HigherWeight = Weight
    elif(Weight < LowerWeight):
        LowerWeight = Weight
print('O maior peso de todos foi: {}'.format(HigherWeight))
print('O menor peso de todos foi: {}'.format(LowerWeight))
