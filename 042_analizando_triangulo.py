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
	print("\nPuede formarse un triangulo", end=" ")
	if a == b == c:
		print("equilatero")
	elif a != b != c != a :
		print("Escaleno")
	else:
		print("isosceles")
else:
	print("\nNo puede formarse un triangulo\n")