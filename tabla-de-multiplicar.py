# def run():
#     contador = 1
#     tabla = int(input('Ingrese el número de la tabla de multiplicar que desea consultar: '))
#     while contador <= 10:
#         print(f'{tabla} X {contador} = {tabla * contador}')
#         contador = contador + 1


def menu():
    x = input('''
            ***¡Bienvenido!***
¿Cuál tabla de multiplicar deseas consultar?:
''')
    print('')
    
    try:
        x = int(x)
    except:
        print('\n¡Error!\nSolo se admiten números enteros.\nIntente de nuevo\n')
    
    return x


def tabla(y):
    z = list(range(1, 11))
    for i in z:
        print(f'{y} X {i} = {y*i}')


def run():
    a = menu()
    while type(a) != int:
        a = menu()
    tabla(a)


if __name__ == '__main__':
    run()
