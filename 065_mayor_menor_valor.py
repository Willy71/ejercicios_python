'''
cree un programa que pida varios numeros enteros por el teclado
En el final, muestre el promedio de todos los numeros, ycual fue
el mayor y el menor valor. El programa debe preguntar en cada
vuelta si el usuario desea continuar
'''
opcion = 's'
resultado = cont = mayor = menor = 0

while opcion != 'n':
    numero = int(input('Digite un numero:           '))
    opcion = str(input('Desea continuar? [S/N]      ')).strip().lower()[0]
    resultado += numero
    cont += 1
    if cont == 1:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        elif numero < menor:
            menor = numero
print('El promedio de los {} numeros ingresados es {}'.format(cont, resultado/cont))
print('El menor numero es {} y el mayor es {}'.format(menor, mayor))