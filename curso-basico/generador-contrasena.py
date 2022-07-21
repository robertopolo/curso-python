import random
import string


def menu():
    selection = input('''***¡Bienvenido al generador de contraseñas!***
Ingrese la cantidad de caracteres que debe poseer su contraseña: ''')
    
    try:
        selection = int(selection)
    except:
        print('\nSolo puede ingresar números. Intente de nuevo.\n')
    
    return selection


def generator(length):
    LOWERCASE = tuple(string.ascii_lowercase)
    UPPERCASE = tuple(string.ascii_uppercase)
    NUMBERS = tuple(string.digits)
    SYMBOLS = tuple(string.punctuation)

    COMBINATION = LOWERCASE + UPPERCASE + NUMBERS + SYMBOLS

    pwd = []
    for i in range(length):
        char_random = random.choice(COMBINATION)
        pwd.append(char_random)
    pwd = ''.join(pwd)
    return pwd


def run():
    length = menu()
    while type(length) != int:
        length = menu()
    x = generator(length)
    print(f'Tu nueva contraseña es: {x}')


if __name__ == '__main__':
    run()
