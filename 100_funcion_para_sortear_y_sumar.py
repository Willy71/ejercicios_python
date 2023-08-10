'''
Cree un programa que tenga una lista llamada numeros
y dos funciones llamadas sorteo() y otra suma_pares().
La primer funcion va a sortear 5 numeros aleatorios
y los va a colocar dentro de la primera lista.
La segunda funcion va a mostrar la suma de los numeros pares
sorteados por la funcion anterior
'''

from random import randint
from time import sleep
from titulo import titular, linea

titular("Sorteo y suma de pares.")
numeros = []


def sorteo():
    for n in range(0, 5):
        numeros.append(randint(0,100))
    print(f'Los 5 numeros sorteados son:   ', end=' ')
    for m in numeros:
        print(f'→ {m}', end=' ', flush=True)
        sleep(1)
    print('listo!!!')
    linea()


def suma_pares(numeros):
    sum_p = 0
    for t in numeros:
        if t%2 == 0:
            sum_p += t
    print(f'La suma de los numeros pares sorteados es {sum_p}')
    linea()

sorteo()
suma_pares(numeros)