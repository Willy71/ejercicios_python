'''
Cree un programa que lea
Nombre, Año de nacimiento, Numero de cartera de trabajo, Edad,
y registrelos en un diccionario. Si el numero de la cartera de trabajo es diferente de cero
agregue, año de cpntratacion y salario. Calcule y agregue, ademas de la edad, con
cuantos años la persona se va a jubilar
'''
from datetime import datetime

trabajo = dict()


trabajo['nombre'] = str(input('Nombre: '))
nacimiento = int(input('Año de nacimiento:  '))
trabajo['edad'] = datetime.now().year - nacimiento
trabajo['cartera'] = int(input('Cartera de trabajo Nº (0 no tiene):  '))
if trabajo['cartera'] != 0:
    trabajo['contratacion'] = int(input('Año de contratacion:   '))
    trabajo['salario'] = float(input('Salario:  '))
    trabajo['jubilacion'] = trabajo['edad'] + ((trabajo['contratacion'] + 35) - datetime.now().year)

print('=-'*30)

print(f'- El nombre de la persona es {trabajo["nombre"]}')
print(f'- Tiene {trabajo["edad"]} años de edad')
print(f'- La cartera de trabajo tiene el numero {trabajo["cartera"]}')
if trabajo['cartera'] != 0:
    print(f'- La contratacion fue en el año {trabajo["contratacion"]}')
    print(f'- El salario tiene un valor de R$ {trabajo["salario"]}')
    print(f'- La jubilacion sera cuando tenga {trabajo["jubilacion"]} años')