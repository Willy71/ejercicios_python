'''
Cree un programa que ingrese por el tecldo varios numeros enteros.
Despues mostrar:
A- Cuantos numeros fueron ingresados
B- La lista de valores ordenada en forma decreciente
C- Si el valor 5 fue digitado y si esta o no en la lista
'''

lista = []
n = []
validar = ''

while True:
    lista.append(int(input('Ingrese un numero entero:       ')))
    validar = str(input('Desea continuar? [S/N]         ')).strip().upper()[0]
    if validar == "N":
        break
print(f'Fueron ingresados {len(lista)} numeros')
print(f'La lista de numeros ordenada en forma decreciente es: {sorted(lista, reverse = True)}')
if 5 in lista:
    print(f'El numero 5 se encuentra en la lista')
else:
    print('El numero 5 no se encuentra en la lista')

