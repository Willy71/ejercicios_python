'''
Cree un programa que lea el primer termino y la razon de una PA
mostrando los 10 primeros resultados usando la estructura while
'''
cont = 1
next = 0
termino = int(input('\33[1;30;45mIngrese el comienzo de la progresion aritmetica:\33[m       '))
razon = int(input('\33[1;30;45mIngrese el interalo de la progresion aritmetica:\33[m       '))
print()
while cont <= 10:
    next += razon
    cont += 1
    print('► \33[1;33m{}\33[m'.format(next), end=" ")
