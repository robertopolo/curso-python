# x = Lista | y = Tupla | z = Diccionario


x = [1, 3, 5, 7, 9]
y = (0, 2, 4, 6, 8)
z = {
    'Nombre completo': 'Roberto Polo',
    'Edad': 33,
    'Estatura': 1.81,
    'Verificado': True
}


print(x)
print(y)
print(z)


print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
print(z['Nombre completo'])
print(z['Edad'])
print(z['Estatura'])
print(z['Verificado'])


for i in x:
    print(i)
for i in y:
    print(i)
for i in z:
    print(i)
for i in z.keys():
    print(i)
for i in z.values():
    print(i)
for i, j in z.items():
    print(f'{i}: {j}')
