'''
Mejore el programa del ejerciocio 93 para que funcione
con varios jugadores incluyendo un sistema de visualizacion
de detalles de aprovechamiento de cada jugador
'''

jugador = {}
resp = ''
lista_total = []
equipo = []
partidos = []
total = 0

while True:
    jugador.clear()
    partidos.clear()
    jugador['nombre'] = str(input('Nombre del jugador:    '))
    total = int(input(f'Cuantos partidos jugo {jugador["nombre"]}:    '))
    for n in range(0, total):
        partidos.append(int(input(f'Cuantos goles en el {n}º juego?:    ')))
    jugador['goles'] = partidos[:]
    jugador['total'] = sum(partidos)
    equipo.append(jugador.copy())
    while True:
        resp = str(input("Desea continuar [S/N]:    ")).strip().upper()[0]
        if resp in "SN":
            break
        print('Error, digite solo S o N:    ')
    if resp == "N":
        break
print('=-'*30)
print('Cod       Nombre                Goles                 Total')
print('-'*60)
for k, v in enumerate(equipo):
    print(f'{k:>2}', end= '')
    for n in v.values():
        print(f'{str(n):^22}', end= '')
    print()
print('-'*60)
busca = 0
while True:
    busca = int(input('Mostrar los datos del jugador número [999 para salir]:   '))
    print('-'*60)
    if busca == 999:
        break
    if busca >= len(equipo):
        print('Error!! No existe jugador con ese codigo.')
        print('-' * 60)
    else:
        print(f'El jugador {equipo[busca]["nombre"]} tuvo el siguiente desempeño')
        print('-' * 60)
        for o, l in enumerate(equipo[busca]["goles"]):
            print(f'        En el juego número {o+1} hizo', end=' ')
            print(f'{l} goles', end=' ')
            print()
        print('-'*60)





    











