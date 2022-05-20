Foods = ('Hamburger', 'Lasagna', 'Meat')
Drinks = ('Coca-Cola', 'Lemon Juice', 'Orange Juice')
Selectioner = int(input('What do you wanna eat?\n[1] For Hamburger\n[2] For Lasagna\n[3] For Meat'))

while True:
    if(Selectioner == 1):
        print("Here's your {}, thanks for buying with us!".format(Foods[0]))
        Stopper = str(input('Do you want something else? [Y/N]: '))
    elif(Selectioner == 2):
        Stopper = str(input('Do you want something else? [Y/N]: '))
        print("Here's your {}, thanks for buying with us!".format(Foods[1]))
    elif(Selectioner == 3):
        print("Here's your {}, thanks for buying with us!".format(Foods[2]))
        Stopper = str(input('Do you want something else? [Y/N]: '))
    if(Stopper in 'Nn'):
        break
    else:
        Selectioner = int(input('What do you wanna eat?\n[1] For Hamburger\n[2] For Lasagna\n[3] For Meat'))
        