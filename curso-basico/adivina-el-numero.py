import random


def run():
    z = True
    while z:
        y = input('Adivina el número (del 1 a 100): ')
        try:
            y = int(y)
        except:
            print('\n¡ERROR!\nEl programa solo admite números enteros.\nIntente de nuevo.\n')
        else:
            z = False


    x = random.randint(1, 100)
    while y != x:
        if y < x:
            print('Elige un número mayor.')
        else:
            print('Elige un número menor.')
        y = int(input('Elige otro número (del 1 a 100): '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()
