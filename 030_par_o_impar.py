"""
cree un programa que pida un numero entero y diga si es par o impar

"""
numero = int(input("Ingrese un numero.entero:\t\t"))

if numero%2 == 0:
	print(f"El numero {numero} es un numero par")
else:
	print(f"El numero {numero} es un numero.impar")