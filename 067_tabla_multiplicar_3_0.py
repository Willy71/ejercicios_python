'''
Cree un programa que muestre la tabla de multiplicar de varios
numeros, uno de cada vez. El programa sera interrumpido al ingresar
un numero negativo
'''
cont = 1
while True:
    print('=-' * 35)
    numero_tabla = int(input('Ingrese un numero entero para su tabla de multiplicar:         '))
    if numero_tabla < 0:
        break
    while cont <= 10:
        print(f'{numero_tabla:^20} X {cont:^20} = {numero_tabla * cont:^20}')
        cont += 1
    cont = 1

