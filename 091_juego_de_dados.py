'''
Cree un programa donde cuatro jugadores tiren un dado
y tengan resultados aleatorios. Guarde esos resultados en un
diccionario. al final coloque ese diccionario en orden
sabiendo que el vencedor tiro el numero mas alto.
'''

from random import randint
from time import sleep
from operator import itemgetter

print('=-'*35)
titulo_uno = "Juego de dados"
print(f'\33[1;30;44m{titulo_uno:^70}\33[m')
print('=-'*35)
titulo_dos = 'Valores sorteados'
print(f'{titulo_dos:^70}')
print('=-'*35)

juego = {'jugador1': randint(1, 6),
         'jugador2': randint(1, 6),
         'jugador3': randint(1, 6),
         'jugador4': randint(1, 6)}

for k, v in juego.items():
    print(f'              El {k} saco el numero {v} en los dados')
    sleep(1)
print('=-'*35)
titulo_tres = 'RANKING DE JUGADORES'
print(f'{titulo_tres:^70}')
print('=-'*35)

ranking = []
ranking = sorted(juego.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
    print(f'                   {k+1} lugar para el {v[0]} con {v[1]}')
    sleep(1)

