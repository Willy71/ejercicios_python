'''
Cree un programa que tenga una funcion llamada
escriba() que reciba un texto cualquiera como
parametro, y muestre un mensaje con tamaño adaptable
Ejemplo:
escriba("Hola Mundo")

salida
=-=-=-=-=-
Hola Mundo
=-=-=-=-=-
'''
from titulo import titular, linea

titular('Un print muy especial.')

def escriba(frase):
    tam = len(frase) + 4
    print('~'*tam)
    print(f'  {frase}')
    print('~'*tam)


frase = str(input('Ingrese una frase como titulo:   '))
escriba(frase)