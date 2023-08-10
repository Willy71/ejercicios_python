'''
cree un programa que pida varios numeros al usuario
El programa solo va a parar cuando el usuario digite 999
En el final muestre cuantos numeros fueron ingresados
y la suma de ellos desconsiderando el numero de salida
(flag)
'''

numero = resultado = contador = 0
numero = int(input('Ingrese un número entero [999 para parar]:      '))

while numero != 999:
    resultado += numero
    contador += 1
    numero = int(input('Ingrese un número entero [999 para parar]:      '))

print('El resultado de la suma de los {} numeros ingresados es {}'.format(contador, resultado))