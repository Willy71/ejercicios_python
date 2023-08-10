'''
Cree un programa que gerencie el desempeño de un jugador de futbol.
El programa va a leer el nombre del jugador y cuantos partidos jugo.
Despues de eso va a leer cuantos goles hizo en cada partido.
En el final todo eso sera guardado en un diccionario incluyendo el total de goles
hechos durante el campeonato
'''
desempeno = {}
partidos = 0
desempeno['jugador'] = str(input('Nombre del jugador:    '))
partidos = int(input('Ingrese la cantidad de partidos:      '))

goles_total = []
total = 0

for n in range(0, partidos):
    goles_total.append(int(input(f'cantidad de goles en el {n+1}º partido:     ')))
    desempeno['goles'] = goles_total

for g in desempeno['goles']:
    total += g
    desempeno['total'] = total

print('=-'*30)
print(desempeno)
print('=-'*30)

for k, v in desempeno.items():
    print(f'El campo {k} tiene el valor {v}')

print('=-'*30)
print(f'El jugador {desempeno["jugador"]} jugo {partidos} partidos')
for i, v in enumerate(desempeno['goles']):
    print(f'        => en el partido {i}, hizo {v} goles.')
print(f'Fue un total de {desempeno["total"]} goles')
print(f'Un promedio de {desempeno["total"]/partidos} goles por partido')