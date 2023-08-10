'''
Cree un programa que tenga una tupla unica con nombres de productos
y sus respectivos precios, en secuencia.
En el final, muestre la lista de precios, organizando los datos
en forma tabular
'''

print('=-'*35)
titulo_uno = 'Lista de precios libreria'
print(f'{titulo_uno:^70}')
print('=-'*35)
lista_precios = ('Lapiz', 5.00, 'Goma', 2.00, 'Cuaderno', 10.00, 'Regla', 7.00, 'Transportador', 3.50, 'Compas', 4.50, 'Mochila', 80.00, 'Lapicera', 7.00, 'Libro', 50.00)
cont = 0

for n in range(0, len(lista_precios)):
    if n%2 == 0:
         print(f'              {lista_precios[n]:.<31}', end = ' ')
    else:
         print(f'R$ {lista_precios[n]:>5}')
print('=-'*35)