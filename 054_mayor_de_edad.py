'''
cree un programa que pida el año de nacimiento de 7 personas
y en el final me diga cuantas personas son mayores de edad
y cuantas son menores
'''

from datetime import date

actual = date.today().year

tot_mayor = 0
tot_menor = 0

for pers in range(1,8):
    nacimiento = int(input("En que año la {}º persona nació:   ".format(pers)))
    edad = actual - nacimiento
    if edad >= 21:
        tot_mayor += 1
    else:
        tot_menor += 1
print("En total tuvimos {} personas mayores de edad".format(tot_mayor))
print('Y {} personas menores de edad'.format(tot_menor))