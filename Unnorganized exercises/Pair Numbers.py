for p in range(1, 21):
    pfake = p % 2
    if(pfake == 0):
        print('{} é par'.format(p))
    else:
        print('{} é impar'.format(p))
