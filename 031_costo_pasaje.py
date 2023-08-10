"""
cree un programa que pida la distancia en Km y calcule el valor del pasaje siendo que sale 0,50 por km hasta 200 km y 0,45 si es.mayor a 200 km

"""

km = float(input("Ingrese la distancia de su viaje en km:\t\t"))

if km <= 200:
	valor = km * 0.50
else:
	valor = km * 0.45
	
print("El valor de su pasaje es de: {:>18} {:>2}".format("R$", valor))