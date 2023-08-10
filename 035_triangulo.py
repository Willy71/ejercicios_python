"""
Para três segmentos fecharem um triângulo, cada lado deve ser menor que a soma dos outros dois.
a < b + c
b < a + c
c < a + b
"""
a = float(input("Ingrese el largo del primer lado de un triangulo:\t"))

b = float(input("\nIngrese el largo del segundo lado de un triangulo:\t"))

c = float(input("\nIngrese el largo del tercer lado de un triangulo:\t"))

if a < (b + c) and b < (a + c) and c < (a + b):
	print("\n{:^20}Puede formarse un triangulo.".format(" "))
else:
	print("\n{:20}No puede formarse un triangulo".format(" "))