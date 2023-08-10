'''
Cree un programa qye lea 4 valores y los guarde en una tupla
En el final analise lo siguiente:
a _ Cuantas veces aparece el numero 9
b _ En que posicion fue digitado el valor 3
c _ Cuales fueron los numeros pares
'''
almacena =  int(input('Ingrese un numero entero:              ')), \
    int(input('Ingrese otro numero entero:            ')), \
    int(input('Ingrese un numero entero mas:          ')), \
    int(input('Ingrese el ultimo numero entero:       '))
print()
print(f'Usted ingreso los siguientes valores: ', end = ' ')
for h in almacena:
    print('-', h, end = ' ')
print()

contar_nueves = almacena.count(9)

if contar_nueves == 1:
    print(f'El numero nueve aparece {contar_nueves} vez.')
else:
    print(f'El numero nueve aparece {contar_nueves} veces.')

if 3 in almacena:
    print(f'El numero tres aparece en la posicion número {almacena.index(3)}')
else:
    print('El valor tres no fue ingresado.')

print('Los valores pares ingresados fueron: ', end =' ')
for n in almacena:
    if n%2 == 0:
       print('-', n, end = ' ')

print()