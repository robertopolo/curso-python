import requests
import datetime
import locale

today = datetime.datetime.now().strftime('%Y-%m-%d')
precio_dolar = round(float(requests.get('https://www.datos.gov.co/resource/ceyp-9c7c.json?vigenciadesde=' + today + 'T00:00:00').json()[0]['valor']),2)

option = int(input('''
***** ¡Bienvenido al conversor! *****
         Elija una opción:
     1.- Convertir pesos a dolares.
     2.- Conventir dolares a pesos.
--------------------------------------
       Ingresa tu opción: '''))

def conversor():
    if option == 1:
        pesos = round(float(input('¿Cuantos pesos desea convertir?: ')),2)
        pesos_dolar = str(round(pesos / precio_dolar,2))
        print('Serian $' + pesos_dolar + ' dolares.')
    elif option == 2:
        dolares = round(float(input('¿Cuantos dolares desea convertir?: ')),2)
        dolar_pesos = str(round(dolares * precio_dolar,2))
        print('Serian $' + dolar_pesos + ' pesos.')
    else:
        print('¡Opción invalida!')

conversor()
