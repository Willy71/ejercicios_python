'''
Cree un programa similar al anterior solo que esta vez
el programa le va a preguntar cuantos terminos mas quiere ver el usuario
El programa se termina cuando coloque cero
Al final muestre cuantos terminos fueron mostrados
'''


print('Generador de progresión aritmetica 3.0')
print('=-'*29)
primer_valor = int(input('\33[1;30;45mIngrese el comienzo de la progresion aritmetica:\33[m       '))
rango = int(input('\33[1;30;45mIngrese el interalo de la progresion aritmetica:\33[m       '))
termino = primer_valor
mas = 10
total = 0
cont = 1

while mas != 0:
    total += mas
    while cont <= total:
        print('\33[1;33m{}\33[m'.format(termino), end=" ► ")
        termino += rango
        cont += 1
    print("PAUSA")
    print('=-' * 29)
    mas = int(input('Cuantos terminos mas quiere ver?:                      '))
print('La progresion finalizo con {} resultados mostrados.'.format(total))
print('=-'*29)