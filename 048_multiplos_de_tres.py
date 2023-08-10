'''
cree un programa que calcule la suma entre todos los numeros impares que son multiplos de
tres y que estan en el intervalo 1 a 500
'''
suma = 0
contador = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        suma += c
        contador += 1
print("La suma de los {} numeros solicitados es de {}".format(contador, suma))