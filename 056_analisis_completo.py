'''
cree un programa que lea nombre, edad y sexo de 4 personas.
En el final del programa mostrar:
La media de edad del grupo
cual es el nombre del hombre mas viejo
cuantas mujeres tienen menos de 20 años
'''

media = 0
hombre_mayor = 0
grabar_nombre = ''
cont_mujeres = 0

for n in range(1, 5):
    print('=='*18)
    print('\33[1;30;44mIngrese los datos de la {}º persona:\33[m'.format(n))
    nombre = str(input('\33[1;30;42mNombre:\33[m                 ')).strip()
    edad = int(input('\33[1;30;42mEdad:\33[m                   '))
    sexo = str(input('\33[1;30;42mSexo (m o f):\33[m           ')).strip().lower()

    media += edad / 4

    if sexo == 'm':
        if edad > hombre_mayor:
            hombre_mayor = edad
            grabar_nombre = nombre
    if sexo == 'f':
        if edad < 20:
            cont_mujeres += 1

print('=='*18)
print('\n\33[1;30;46mLa edad media del grupo es de {} años\33[m'.format(media))
print('\33[1;30;46mEl hombre mas viejo del grupo tiene {} y se llama {}\33[m'.format(hombre_mayor, grabar_nombre))
if cont_mujeres == 1:
    print('\33[1;30;46mEl grupo tiene {} mujer con menos de 20 años\33[m'.format(cont_mujeres))
elif cont_mujeres == 0:
    print('\33[1;30;46mEl grupo NO tiene mujeres con menos de 20 años\33[m'.format(cont_mujeres))
else:
    print('\33[1;30;46mEl grupo tiene {} mujeres con menos de 20 años\33[m'.format(cont_mujeres))