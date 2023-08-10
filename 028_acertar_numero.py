"""
programa que piense un numero entre 0 y 5 y la persona intente descubrir
"""

import random

num_al = random.randint(0,5)

usuario = int(input("Adivine el número entre 0 y 5:\t"))

if usuario == num_al:
	print("Acerto el numero era el {}. Felicitaciones!!!".format(num_al))
else:
	print("No acerto!! El numero era el {}.".format(num_al))