'''
cree un programa que lea 5 valores numericos ingresados por el usuario
y los guarde en una lista
Al final mostrar cual fue el menor, cual el mayor.
Los numeros ingresados y las respectivas posiciones en esa lista.
'''
lista = []
menor = mayor = cont = 0

for n in range(0,5):
    lista.append(int(input(f'Ingrese el valor {n+1}:       ')))
    if n == 0:
        menor = mayor = lista[n]
    else:
        if lista[n] < menor:
            menor = lista[n]
        if lista[n] > mayor:
            mayor = lista[n]
print()
print(f'El menor numero ingresado fue el {menor} y aparece en  ', end = ' ')
for b, c in enumerate(lista):
    if c == menor:
        print(f'{b} ', end = '.. ')
print(' lugar')

print(f'\nEl mayor numero ingresado fue el {mayor} y aparece en  ', end = ' ')
for d, e in enumerate(lista):
    if e == mayor:
        print(f'{d}', end = '.. ')
print(' lugar')
