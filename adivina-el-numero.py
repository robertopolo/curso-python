import random


def run():
    x = random.randint(1, 100)
    y = int(input('Adivina el número (del 1 a 100): '))
    while y != x:
        if y < x:
            print('Elige un número mayor.')
        else:
            print('Elige un número menor.')
        y = int(input('Elige otro número (del 1 a 100): '))
    print('¡Ganaste!')



if __name__ == '__main__':
    run()
