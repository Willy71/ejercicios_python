'''
Cree un programa que tenga una funcion llamada mayor()
que reciba varios parametros con valores enteros
Su programa tiene que analizar todos los numeros
y decir cual es el mayor
'''

from titulo import titular, linea

titular("Cual es el mayor?")

def mayor(lista_dos):
    may = cont = 0
    for n in range(0, len(lista_dos)):
        if n == 0:
            may = lista_dos[n]
        elif lista_dos[n] > may:
            may = lista_dos[n]
    linea()
    print(f'Fueron ingresados {len(lista_dos)} valores')
    print(f'Los valores fueron: ', end='')
    for n in lista_dos:
        print(f'- {n}', end=' ')
    print()
    print(f'El mayor numero ingresado fue el {may}.')
    linea()

validar = ''
lista_dos = []
validar_dos = ''

while True:
    num = int(input('Ingrese un numero entero:  '))
    lista_dos.append(num)
    validar = str(input('Desea continuar [S/N]?: ')).strip().upper()[0]
    if validar == 'N':
        break


mayor(lista_dos)