numero = 1234567456456.89
miles_translator = str.maketrans(".,", ",.")
numero = f"{numero:,}".translate(miles_translator)
print(numero)
# O si no quieres usar f-strings:

miles_translator = str.maketrans(".,", ",.")
numero = "{:,}".format(numero).translate(miles_translator)