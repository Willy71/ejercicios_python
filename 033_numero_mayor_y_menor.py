num_1 = int(input("Ingrese un número (1 de 3)\t"))

num_2 = int(input("\nIngrese un número (2 de 3)\t"))

num_3 = int(input("\nIngrese un número (3 de 3)\t"))

if num_1 > num_2 and num_1 > num_3:
	print("\n		{} es el mayor de los tres".format(num_1))
elif num_2 > num_1 and num_2 > num_3:
	print("\n		{} es el mayor de los tres".format(num_2))
else:
	print("\n		{} es el mayor de los tres".format(num_3))
	
if num_1 < num_2 and num_1 < num_3:
	print("\n		{} es el menor de los tres".format(num_1))
elif num_2 < num_1 and num_2 < num_3:
	print("\n		{} es el menor de los tres".format(num_2))
else:
	print("\n		{} es el menor de los tres".format(num_3))