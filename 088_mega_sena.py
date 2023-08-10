'''
Cree un programa que ayude a un jugador de loteria a crear
sus apuestas. El programa va a preguntar cuantos juegos quiere que
sean generados y va a sortear 6 numeros entre 1 y 60, registrando todo
en una lista compuesta
'''
from random import randint
from time import sleep

print('=-'*35)
print('\33[1;30;44m                          Juego de loteria                            \33[m')
print('=-'*35)
print()
cantidad = int(input('Cuantos juegos aleatorios desea crear?    '))
print()
num = 0
tot = 1
lista = []
juegos = []

while tot <= cantidad:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    juegos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*12, f'SORTEANDO {cantidad} JUEGOS', '=-'*13)
print()
for j, l in enumerate(juegos):
    print(f'El {j+1}º sorteo es         {l}')
    sleep(2)
print()
frase = 'BUENA SUERTE'
print('=-'*14, f'{frase}', '=-'*14)


