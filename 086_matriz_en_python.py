'''
Cree un programa que cree una matriz de 3 x 3 y rellene
con valores ingresados por el teclado.

En el final muestre la matriz en pantalla con
la formacion correcta
'''
lineas = [[], [], []]
valor = 0

for b in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Ingrese un valor para {[b, c]}      '))
        lineas[b].append(valor)

print('=-'*20)

for u in range(0, 3):
    for t in range(0, 3):
        print(f'[{lineas[u][t]:^4}]', end = ' ')
    print()
