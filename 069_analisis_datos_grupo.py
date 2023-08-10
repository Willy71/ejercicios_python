'''
cree un programa que pida la edad y el sexo de cada persona
al finalizar cada ingreso que pregunte si desea continuar
Al finalizar mostrar:
Cuantos tienen mas de 18
Cuantos son hombres
Cuantas mujeres tienen menos de 20
'''
print('=-'*25)
print('\33[1;30;44m         Programa para ingreso de datos           \33[m')

suma_may_18 = suma_hombre = suma_fem = 0

while True:
    print('=-'*25)
    edad = int(input('Ingrese la edad:                 '))
    sexo = str(input('Ingrese el sexo [M/F]            ')).strip().upper()[0]

    if sexo == 'M':
        suma_hombre += 1
    if edad >= 18:
        suma_may_18 += 1
    if sexo == 'F' and edad < 20:
        suma_fem += 1

    continuar = ' '
    while continuar not in 'SN':
        print('=-' * 25)
        continuar = str(input('Desea continuar? [S/N]           ')).strip().upper()[0]

    if continuar == "N":
        break

print('=-'*25)
print('\33[1;30;44m               Fin del programa!!!                \33[m')
print('=-'*25)
print(f'Son {suma_may_18} personas con mas de 18 años')
print(f'Son {suma_hombre} hombres')
print(f'Y hay {suma_fem} mujeres menores de 20 años')
print('=-'*25)


