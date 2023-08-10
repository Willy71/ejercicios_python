'''
Cree un programa que lea el nombre y dos notas de cada alumno y
guarde todo en una lista compuesta . En el final, muestre el boletin
Conteniendo la media de cada alumno y permita despues mostrar las
notas de cada alumno en forma individual
'''
print('=-'*30)
print('\33[1;30;44m                Boletin de calificaciones                   \33[m')
print('=-'*30)

lista_notas = []
alumno = []
validacion = ''

while True:
    lista_notas.append(str(input('Nombre:     ')))
    for n in range(1, 3):
        lista_notas.append(float(input(f'Ingrese la {n}º nota:   ')))
    alumno.append(lista_notas[:])
    lista_notas.clear()
    print('=-'*30)
    validacion = str(input('Desea continuar? [S/N]     ')).strip().upper()[0]
    print('=-'*30)
    if validacion == 'N':
        break
print('No.      NOME        MEDIA')
print('=-'*15)
promedio = 0
for b in range(0, len(alumno)):
    print(f'{b:<8}', end = ' ')
    for c in range(0, 1):
        print(f'{alumno[b][c]:<12}', end = ' ')
        promedio = (alumno[b][1]+alumno[b][2])/2
        print(promedio)
print('=-'*15)

nombrar = 0
while True:
    nombrar = int(input('Ingrese el número de alumno. Para concluir digite [999]:   '))
    print('=-' * 30)
    print(f'Las notas de {alumno[nombrar][0]} son {alumno[nombrar][1]} y {alumno[nombrar][2]}')
    print('=-' * 30)
    if nombrar == 999:
        break

