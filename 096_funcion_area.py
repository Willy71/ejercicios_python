'''
Haga un programa que tenga una funcion llamada area
que reciba las dimensiones de un terreno rectangular
(ancho y largo) y muestre el area del terreno
'''
from titulo import titular, linea

titular('Area del terreno')

a = float(input('Ingrese el largo del terreno:  '))
b = float(input('Ingrese el ancho del terreno:  '))
linea()

def area(a, b):
    total = a * b
    print(f'El area de un terreno de {a} mts x {b} mts es de {total} mts²')


area(a, b)