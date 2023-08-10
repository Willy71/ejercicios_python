'''
Cree un programa en donde el usuario digite 5 valores enteros
y los incluya en una lista ya en la posicion correcta ordenada.

No utilizar la funcion sort()
'''

lista = l = []
cont = 0
ant = 0


for m in range(0, 5):
    l = int(input(f'Ingrese el {m+1}º valor.      '))
    if m == 0 or l > lista[-1]:
        lista.append(l)
    else:
        pos = 0
        while pos < len(lista):
            if l <= lista[pos]:
                lista.insert(pos, l)
                break
            pos += 1
print('=-'*30)
print(f'Los valores digitados en orden son {lista}')



