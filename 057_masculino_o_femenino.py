'''
Cree un programa que lea el sexo de una persona
que solo acepte valores F o M
Caso este errado pida que digite nuevamente
hasta tener un valor correcto
'''

sexo = str(input('Ingrese su sexo con (F/M):        ')).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input('Datos no validos, por favor indique su sexo:      ')).strip().upper()[0]
print('Sexo {} registrado con exito'.format(sexo))