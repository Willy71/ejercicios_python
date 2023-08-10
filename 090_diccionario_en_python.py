'''
Haga un programa que lea el nombre y la media de un alumno
guardando tambien la situacion (Reprobado [entre 0 y 7],
aprobado [encima de 7]) en un diccionario
En el final muestre el contenido de la estructura en la pantalla
'''
alumnos = {}
alumnos['nombre'] = str(input('Nombre: '))
alumnos['nota'] = float(input('Nota:   '))
print('='*50)
print(f'    - El nombre es {alumnos["nombre"]}')
print(f'    - La nota fue {alumnos["nota"]}')
if alumnos['nota'] >= 7:
    alumnos['situacion'] = 'APROBADO'
elif alumnos['nota'] < 7 and alumnos['nota'] >= 5:
    alumnos['situacion'] = 'RECUPERACION'
else:
    alumnos['situacion'] = 'REPROBADO'
print(f'    - Situacion = {alumnos["situacion"]}')




