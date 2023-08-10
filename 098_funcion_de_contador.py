'''
Cree un programa que tenga una funcion llamada contador()
que reciba tres parametros: Inicio, fin y paso.
Su programa tiene que hacer tres cuentas a traves de la
funcion creada:

A- de 1 hasta 10 de 1 en 1
B- de 10 hasta 0 de 2 en 2
C- Cuenta personalizada
'''
from titulo import titular, linea
from time import sleep

def contador(i, f , p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        print(f'La cuenta regresiva de {i} hasta {f} de {p} en {p} es:')
        for n in range(i, f-1, -p):
            print(f'{n}', end=' ', flush=True)
            sleep(1/2)
    elif f > i:
        print(f'La cuenta ascendente de {i} hasta {f} de {p} en {p} es:')
        for n in range(i, f+1, p):
            print(f'{n}', end=' ', flush=True)
            sleep(1/2)


linea()
contador(1, 10, 1)
print()
linea()
contador(10, 0, 2)
print()
linea()

print("Ahora es su turno de colocar los datos de la cuenta:     ")
a = int(input('Ingrese un numero entero como inicio:    '))
b = int(input('Ingrese un numero entero como fin:   '))
c = int(input('Ingrese un numero entero como paso:  '))
linea()
contador(a, b, c)
print()
linea()