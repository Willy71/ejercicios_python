'''
Cree un programa que lea el nombre y el precio de un producto.
El program debe preguntar si quiere continuar en cada ingreso.
Al final muestre:
Cual es el total de la compra
Cuantos productos cuestan mas de R$ 1000
Cual es el nombre del producto mas barato
'''

nombre_producto_barato = ''
total = cont = suma = mas_de_mil = menor = 0

print('=-'*35)
print('\33[1;30;44m                     Programa para ingreso de datos                   \33[m')

while True:
    print('=-' * 35)
    cont += 1
    nombre = str(input('Ingrese el nombre del producto:         '))
    precio = float(input('Ingrese el valor del producto:          '))
    suma += precio

    if precio > 1000:
        mas_de_mil += 1

    if cont == 1:
        menor = precio
        nombre_producto_barato = nombre

    if precio < menor:
        menor = precio
        nombre_producto_barato = nombre

    continuar = ' '
    while continuar not in 'SN':
        print('=-' * 35)
        continuar = str(input('Desea continuar? [S/N]                       ')).strip().upper()[0]

    if continuar == 'N':
        break

print('=-' * 35)
print('\33[1;30;44m                          Fin del programa!!!                         \33[m')
print('=-'*35)
print(f'La suma de todos los productos comprados es de R${suma}')
print(f'La cantidad de productos que salen mas de R$1000 es de {mas_de_mil} productos')
print(f'El nombre del producto mas barato es {nombre_producto_barato} y su valor es de R${menor}')
print('=-'*35)