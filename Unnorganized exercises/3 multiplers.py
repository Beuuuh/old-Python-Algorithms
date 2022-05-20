Plus = 0
counter = 0
for n in range(1, 501, 2):
    if(n % 3 == 0):
        Plus += n
        counter += 1
print('Os valores: {} somados é: {}'.format(counter, Plus))
