import requests
from datetime import datetime, timedelta
import operator

today = datetime.now()
url = 'https://www.datos.gov.co/resource/ceyp-9c7c.json?vigenciadesde='
separators = str.maketrans('.,', ',.')


def get_trm(actual_date):
    x = requests.get(url + actual_date.strftime('%Y-%m-%d') + 'T00:00:00').json()
    while len(x) == 0:
        actual_date = actual_date - timedelta(1)
        x = requests.get(url + actual_date.strftime('%Y-%m-%d') + 'T00:00:00').json()
    return round(float(x[0]['valor']), 2)


def menu(actual_dolar_price):
    y = ''
    MENU_OPTIONS = (1, 2)
    while True:
        y = input(f'''
                       ***** ¡Bienvenido al conversor! *****
     ___________________________________________________________________________
    |                                                                           |
    | El precio del dolar para el día de hoy es de: ${actual_dolar_price} pesos |
    |___________________________________________________________________________|
                                 Elija una opción:
                           1.- Convertir pesos a dolares.
                           2.- Conventir dolares a pesos.
    -----------------------------------------------------------------------------
                             Ingresa tu opción: \n''')
        print('')
        try:
            y = int(y)
        except:
            print('¡ERROR! La opción ingresada no es valida. Intente de nuevo.')
        else:
            if y not in MENU_OPTIONS:
                print('¡ERROR! La opción ingresada no es valida.Intente de nuevo.')
                continue
            else:
                return y


def conversor(option_selected, dolar):
    z = ''
    a = ('pesos', 'dolares')
    b = (operator.truediv, operator.mul)
    while type(z) != int:
        z = input(f'¿Cuantos {a[option_selected - 1]} deseas convertir?: ')
        try:
            z = int(z)
        except:
            print('¡ERROR! Elija una opción correcta.')
    
    c = round(float(b[option_selected - 1](z, dolar)), 2)
    c = f'{c:,}'.translate(separators)
    print(f'Serian $ {c} {a[option_selected * - 1]}')
    

def run():
    dolar_price = get_trm(today)
    selection = menu(dolar_price)
    conversor(selection, dolar_price)

if __name__ == '__main__':
    run()