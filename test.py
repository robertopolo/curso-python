import locale

ubication = locale.getlocale()
locale.setlocale(locale.LC_ALL, ubication)
valor = 2750000
dinero = '{:,d}'.format(valor) 

print(ubication)
print(dinero)

