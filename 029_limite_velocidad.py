"""
Escriba un programa que pida la velocidad de un auto.
Si la velocidad es superior a 80 km/h el conductor recibe una multa de R$ 7 por km excedente
"""

velocidad = int(input("Ingrese la velocidad por la que paso el control:\t"))

if velocidad > 80:
	multa = (velocidad-80)*7
	print("\nLa multa que usted recibira por pasar a {} km/h es de R${} ".format(velocidad, multa))
else:
	print("\nUsted es un conductor responsable, FELICITACIONES!!")