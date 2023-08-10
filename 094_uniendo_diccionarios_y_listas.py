'''
Cree un programa que lea nombre, sexo y edad de varias personas.
guardando los datos de cada persona en un diccionario y todos los
diccionarios en una lista.
En el final muestre
A- Cuantas personas fueron registradas
B- La media de las edades
C- La lista de mujeres
D- Una lista con edad encima de la media
'''

diccionario_princ = {}
lista_datos = []
validar = ''
cont = edad = 0

while True:
    diccionario_princ.clear()
    diccionario_princ['nombre'] = str(input('Nombre   '))
    while True:
        diccionario_princ['sexo'] = str(input('Sexo [M/F]   ')).strip().upper()[0]
        if diccionario_princ['sexo'] in 'MF':
            break
        print('Error!!! Por favor digite solo M o F:   ')
    diccionario_princ['edad'] = int(input('Edad:   '))
    lista_datos.append(diccionario_princ.copy())
    cont += 1
    edad += diccionario_princ['edad']
    while True:
        validar = str(input('Desea continuar [S/N]:   ')).strip().upper()[0]
        if validar in 'SN':
            break
        print('Error!!, coloque solo S o N:   ')
    if validar == 'N':
        break
#print(lista_datos)
print('=-' * 40)
print(f'A - Tenemos {cont} personas registradas.')
print(f'B - El promedio de edad es de {edad / cont:.2f} años.')

print(f'C - Las mujeres en el listado son:', end=' ')
for k in lista_datos:
    if k["sexo"] in "F":
        print(f'{k["nombre"]}', end=' ')
print()

print(f'D - Lista de personas que estan encima de la media de edad:', end=' ')
for y in lista_datos:
    if y["edad"] > (edad/cont):
        print(f'{y["nombre"]}', end=' ')
print()
print('=-'*40)

