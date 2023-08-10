'''
Cree un programa con una tupla llena de una cuenta en letras de cero a veinte.
Su programa debera leer un numero por el teclado (de 0 a 20) y mostrarlo en letras
'''

cuenta_en_letras = ('cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisiete', ' dieciocho', 'diecinueve', 'veinte')

while True:
    numero = int(input('Ingrese un número de cero a veinte [0 a 20]:        '))
    if numero < 0 or numero > 20:
        print('=-'*27)
        print('Por favor ingrese un número valido')
    elif numero >= 0 or numero <= 20:
        print('=-'*27)
        print(f'El número que usted digito es el \33[1;33m{cuenta_en_letras[numero]}\33[m')
        print('=-'*27)
        break
