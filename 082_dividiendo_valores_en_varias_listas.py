'''
Cree un programa que ingrese varios numeros por el teclado
y los coloque en una lista.
Despues de eso cree dos listas extras, una de pares y otra de impares.
Al final muestre las tres listas generadas
'''

lista = []
lista_par = []
lista_impar = []
validar = ''

while True:
    lista.append(int(input('Ingrese un valor entero:        ')))
    validar = str(input('Desea continuar? [S/N]           ')).strip().upper()[0]
    if validar == "N":
        break
print('=-'*28)
for n in lista:
    if n%2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(f'La lista completa es : {lista}')
print(f'La lista de numeros pares es: {lista_par}')
print(f'La lista de numeros impares es: {lista_impar}')


