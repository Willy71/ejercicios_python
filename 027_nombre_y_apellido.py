"""
haga un programa que pida el nombre completo y devuelva el primer nombre y el apellido separadamente
"""
nombre_completo = str(input("Ingrese su nombre completo:\t"))

lista = nombre_completo.split()

print("\nSu primer nombre es: {}".format(lista[0]))

print("\nSu apellido es: {}".format(lista[-1]))