'''
Cree un programa donde el usuario pueda digitar varios valores
numericos.
En el caso que el numero ya haya sido ingresado, no lo tenga en cuenta.
El final seran exhibidos todos los numeros unicos en orden ascendente.
'''
numeros = n = []
validar = ''


while True:
    n = int(input('Ingrese un valor entero:        '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado con exito.')
    else:
        print('El valor no sera adicionado')
    validar = str(input('Desea continuar [S/N] ?:       ')).strip().upper()[0]
    if validar == 'N':
        break

print(sorted(numeros))

