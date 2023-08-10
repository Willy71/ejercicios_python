from random import shuffle

nome_1 = input("Ingrese el nombre del primer alumno:\t\t")

nome_2 = input("\nIngrese el nombre del segundo alumno:\t\t")

nome_3 = input("\nIngrese el nombre del tercer alumno:\t\t")

nome_4 = input("\nIngrese el nombre del cuarto alumno:\t\t")

lista = [nome_1, nome_2, nome_3, nome_4]

shuffle(lista)

print("\nEl orden de los presentadores sera la siguiente:\n")
for x in lista:
	print("{:>55}\n".format(x))

"""
lista = []
lista_dos = []
cont = 0

while cont < 4:
	num = random.randint(1, 4)
	lista.append(num)
	for x in lista:
		if x not in lista_dos:
			lista_dos.append(x)
			cont += 1

for azar in lista_dos:
	if azar == 1:
		print("\nPrimera persona es {:^27}".format(nome_1))
	elif azar == 2:
		print("\nSegunda persona es {:^27}".format(nome_2))
	elif azar == 3:
		print("\nTercera persona es {:^27}".format(nome_3))
	elif azar == 4:
		print("\nCuarta persona es {:^27}".format(nome_4))
	else:
		print("Error")
"""