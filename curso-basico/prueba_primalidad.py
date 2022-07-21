def primalidad(x):
    contador = 0
    for i in range(2, x):
        if x % i == 0:
            contador += 1
            break
    if contador == 0:
        print('Es primo')
    else:
        print('No es primo')


def run():
    x = int(input('Ingresa un número: '))
    primalidad(x)


if __name__ == '__main__':
    run()
