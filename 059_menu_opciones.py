'''
cree un programa que lea dos valores
y muestre un menu como el de abajo.
Su programa realizara la accion indicada en cada caso.

[1] Sumar
[2] Multiplicar
[3] Mayor
[4] Nuevos numeros
[5] Salir del programa
'''
salir = False
salida = 0

numero_uno = int(input('Ingrese el primer numero entero:         '))
numero_dos = int(input('Ingrese el segundo numero entero:        '))

while salir == False:
    print('==-'*16)
    print('[1] Sumar\n[2] Multiplicar\n[3] Mayor\n[4] Nuevos numeros\n[5] Salir del programa ')
    print('==-'*16)
    opcion = int(input('Ingrese su opcion:                        '))
    print('==-'*16)
    if opcion == 1:
        salida = numero_uno + numero_dos
        print('La suma de {} mas {} es {}'.format(numero_uno, numero_dos, salida))
    elif opcion == 2:
        salida = numero_uno * numero_dos
        print('La multiplicacion de {} por {} es igual a {}'.format(numero_uno, numero_dos, salida))
    elif opcion == 3:
        if numero_uno > numero_dos:
            print('El numero {} es mayor que el numero {}'.format(numero_uno, numero_dos))
        else:
            print('El numero {} es mayor que el numero {}'.format(numero_dos, numero_uno))
    elif opcion == 4:
        numero_uno = int(input('Ingrese el primer numero entero:         '))
        numero_dos = int(input('Ingrese el segundo numero entero:        '))
    elif opcion == 5:
        salir = True
print('Usted eligio salir del programa')
print('==-'*16)