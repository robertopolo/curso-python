# palabra_frase = input('Ingrese la palabra o frase a comprobar: ')
# palabra_frase = palabra_frase.lower().replace(' ', '')
# print(palabra_frase)

def palindromo(palabra_frase):
    palabra_frase_invertida = palabra_frase[::-1]
    if palabra_frase == palabra_frase_invertida:
        return True
    else:
        return False

def run():
    texto_ingresado = input('Ingresa la palabra o frase a comprobar: ').lower().replace(' ', '')
    es_palindromo = palindromo(texto_ingresado)
    if es_palindromo:
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()