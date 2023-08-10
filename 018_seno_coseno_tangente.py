import math

grado = float(input("Ingrese un valor de grados de 0 a 360:\t\t"))

rad = math.radians(grado)

seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)

print("\nEl seno de {} es:{:>34.2f}".format(grado, seno))
print("\nEl coseno de {} es:{:>32.2f}".format(grado, coseno))
print("\nLa tangente de {} es:{:>30.2f}".format(grado, tangente))