'''
Cree un programa con una tupla rellena con los 20 primeros equipos del futbol
Argentino de Primera division.
Muestre despues:
A- Los 5 primeros
B- Los 4 ultimos
C- Equipos en orden alfabetico
D - En que posicion esta Rosario
'''
print('=-'*70)
titulo = 'Lista de los primeros 20 equipos de la primera division del Futbol Argentino'
print(f'\33[1;30;44m{titulo:^140}\33[m')
print('=-'*70)
equipos_futbol = ('River Plate', 'San Lorenzo', 'Defensa y Justicia', 'Lanus',
'Belgrano', 'Talleres', 'Estudiantes', 'Rosario',
'Godoy Cruz', 'Tigre', 'Argentinos Juniors', 'Newell`s Old Boys',
'Boca Juniors', 'Racing', 'Central Cordoba', 'Platense',
'Colon', 'Barracas Central', 'Instituto', 'Velez Sarsfield')

for c in range(0, 5):
    print(f'{c+1:^6} - {equipos_futbol[c]:<18}', end ="")
print()
for d in range(5, 10):
    print(f'{d + 1:^6} - {equipos_futbol[d]:<18}', end="")
print()
for e in range(10, 15):
    print(f'{e + 1:^6} - {equipos_futbol[e]:<18}', end="")
print()
for f in range(15, 20):
    print(f'{f + 1:^6} - {equipos_futbol[f]:<18}', end="")
print()
print('=-'*70)
seg_titulo = 'Los 5 primeros equipos de la liga son:'
print(f'\33[1;30;44m{seg_titulo:^140}\33[m')
print('=-'*70)
for g in range(0, 5):
    print(f'{g+1:^6} - {equipos_futbol[g]:<18}', end ="")
print()
print('=-'*70)
tercer_titulo =' Los 4 equipos que estan en zona de descenso son: '
print(f'\33[1;30;44m{tercer_titulo:^140}\33[m')
print('=-'*70)
for h in range(16, 20):
    print(f'{equipos_futbol[h]:^35}', end ="")
print()
print('=-'*70)
cuarto_titulo = 'Equipos en orden alfabetico'
print(f'\33[1;30;44m{cuarto_titulo:^140}\33[m')
print('=-'*70)
print(f'{sorted(equipos_futbol)[0:5]}', end =' ')
print()
print(f'{sorted(equipos_futbol)[5:10]}', end =' ')
print()
print(f'{sorted(equipos_futbol)[10:15]}', end =' ')
print()
print(f'{sorted(equipos_futbol)[15:20]}', end =' ')
print()
print('=-'*70)
quinto_titulo = 'Posicion de Rosario Central'
print(f'\33[1;30;44m{quinto_titulo:^140}\33[m')
print('=-'*70)
print(f'Rosario central esta en {equipos_futbol.index("Rosario")+1}º posición.')
print('=-'*70)
