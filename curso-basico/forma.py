import math


def menu():
    selection = input('Ingrese la extensión de la forma: ')
    
    try:
        selection = int(selection)
    except:
        print('¡Error!\nEl programa solo se ejecuta con números enteros.\nIntente de nuevo\n')
    
    return selection


def run():
    resta = 2
    forma = '+'
    numero = menu()
    while type(numero) != int:
        numero = menu()
    for i in range(numero):
        if i < math.ceil(numero / 2):
            print(forma * i)
        else:
            print(forma * (i - resta))
            resta += 2


if __name__ == '__main__':
    run()
