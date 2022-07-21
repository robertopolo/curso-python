def run():
    limite = 1000
    contador = 0
    potencia = 2**contador

    while potencia < limite:
        print(f'2 elevado a {contador} es igual a : {potencia}')
        contador = contador + 1
        potencia = 2**contador


if __name__ == '__main__':
    run()