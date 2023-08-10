import random

nome_1 = str(input("Ingrese el nombre del primer alumno:\t\t"))

nome_2 = str(input("\nIngrese el nombre del segundo alumno:\t\t"))

nome_3 = str(input("\nIngrese el nombre del tercer alumno:\t\t"))

nome_4 = str(input("\nIngrese el nombre del cuarto alumno:\t\t"))

lista = [nome_1, nome_2, nome_3, nome_4]

elegido = random.choice(lista)

print("\nLa persona elegida es {:^32}".format(elegido))

"""
azar = random.randint(1,4)

if azar == 1:
	print("\nLa persona elegida es {:>27}".format(nome_1))
elif azar == 2:
	print("\nLa persona elegida es {:>27}".format(nome_2))
elif azar == 3:
	print("\nLa persona elegida es {:>27}".format(nome_3))
elif azar == 4:
	print("\nLa persona elegida es {:>27}".format(nome_4))
else:
	print("Error")
"""