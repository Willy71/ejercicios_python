'''
Cree un programa que calcule el factorial de un numero
ingresado por el usuario.

El factorial de un numero n es el producto de la multiplicacion
de todos sus antecesores mayores que cero.
'''

numero_usuario = int(input('\33[1;30;44mIngrese un numero entero:\33[m           '))
resultado = 1
contador = 0

while contador < numero_usuario:
    resultado = resultado * (contador + 1)
    contador += 1

print('\n\33[1;30;43mEl  numero  factorial  de  {}  es  {}\33[m'.format(numero_usuario, resultado))