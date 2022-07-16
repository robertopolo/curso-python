# def run():
#     contador = 1
#     tabla = int(input('Ingrese el número de la tabla de multiplicar que desea consultar: '))
#     while contador <= 10:
#         print(f'{tabla} X {contador} = {tabla * contador}')
#         contador = contador + 1
def tabla_multiplicar(numero):
    multiplicador = [1,2,3,4,5,6,7,8,9,10]
    for i in multiplicador:
        print(f'{numero} X {i} = {numero*i}')


def run():
    multiplicando = input('Ingrese el número del que desea conocer la tabla de multiplicar: ')
    try:
        int(multiplicando)
    except:
        print('¡Error! El programa solo acepta números. Intente de nuevo')
    tabla_multiplicar(multiplicando)


if __name__ == '__main__':
    run()
