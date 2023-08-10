'''
Cree un programa que genere 5 numeros aleatorios
y los coloque en una tupla
Despues de eso, mostrar los 5 numeros generados y cual es el mayor
y cual el menor
'''

from random import randint

aleatorios = (randint(1, 4), randint(5, 8), randint(9, 12), randint(13, 16), randint(17, 20))
print('Los valores sorteados fueron:   ', end = '')
for n in aleatorios:
    print(f'{n}', end = " ")
print()
print(f'El mayor valor sorteado fue: {max(aleatorios)}')
print(f'El menor valor sorteado fue: {min(aleatorios)}')
