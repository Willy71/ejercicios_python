'''
Cree un programa donde el usuario pueda ingresar siete valores
numericos y registralos en una lista unica que mantenga separados los valores pares e impares
Al final muestre los valores pares e impares en forma cresciente
'''
valor = 0
lista = [[], []]

for n in range(1, 8):
    valor = int(input(f"Ingrese el {n}º número entero: "))
    if valor%2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print('=-'*30)
print(f'Los valores pares ingresados fueron: {sorted(lista[0])}')
print(f'Los valores impares ingresados fueron: {sorted(lista[1])}')
