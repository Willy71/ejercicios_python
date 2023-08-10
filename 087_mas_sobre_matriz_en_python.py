'''
Copie y pegue el desafio anterior solo que en el final va a mostrar:

A- Suma de todos los valores pares digitados
B- Suma de los valores de la tercera columna
C- el mayor valor de la segunda linea
'''
lineas = [[], [], []]
valor = 0
suma_total = 0
suma_linea_tres = 0
mayor = 0
for b in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Ingrese un valor para {[b, c]}      '))
        lineas[b].append(valor)
        suma_total += valor
        if b == 2:
            suma_linea_tres += valor
        if b == 1:
            if lineas[b][c] == lineas[1][0]:
                mayor = valor
            elif lineas[b][c] > mayor:
                mayor = lineas[b][c]

print('=-'*20)

for u in range(0, 3):
    for t in range(0, 3):
        print(f'[{lineas[u][t]:^4}]', end = ' ')
    print()
#=========================================================================

print('=-'*20)
print(f'La suma de todos los valores ingresados es {suma_total}')
print(f'La suma de los valores de la tercera linea es {suma_linea_tres}')
print(f'El mayor numero de la segunda linea es {mayor}')