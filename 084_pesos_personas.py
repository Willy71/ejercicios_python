'''
Hga un programa que lea el peso de varias personas guardando
todo en un lista
al final muestre:
A_ Cuantas personas fueron registradas
B_ Una lista con las personas mas pesadas
C_Una lista con las personas mas livianas
'''
personas = []
lista_total = []
lista_pesados = []
lista_livianos = []
validar = ''
cont = 0
menor = mayor = 0
while True:
    personas.append(str(input('Nombre: ')))
    personas.append(float(input('Peso: ')))
    lista_total.append(personas[:])
    personas.clear()
    validar = str(input('Desea continuar [S/N]: ')).strip().upper()[0]
    cont += 1
    if validar == 'N':
        break
cont_dos = 0
while cont_dos < len(lista_total):
    if cont_dos == 0:
        menor = lista_total[0][1]
        mayor = lista_total[0][1]
    if lista_total[cont_dos][1] < menor:
        menor = lista_total[cont_dos][1]
    if lista_total[cont_dos][1] > mayor:
        mayor = lista_total[cont_dos][1]
    cont_dos += 1

print('=-'*30)
print(f'Fueron registradas {cont} personas.')
print(f'El menor peso fue de {menor} kls y fue de: ', end = ' ')
for k in lista_total:
    if k[1] == menor:
        print(f'{k[0]}', end = ', ')

print(f'\nEl mayor peso fue de {mayor} kls y fue de: ', end = ' ')
for t in lista_total:
    if t[1] == mayor:
        print(f'{t[0]}', end = ', ')
print()
print('=-'*30)