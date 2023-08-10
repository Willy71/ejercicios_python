""" 
programa que calcule la hipotenusa de un triangulo rextangulo, teniendo la medida del cateto opuesto, del cateto adyacente

"""
print("Calculemos la hipotenusa de un triangulo rectangulo.\n")

opuesto = float(input("Ingrese la medida del cateto opuesto:\t\t"))

adyacente = float(input("\nIngrese la medida del cateto adyacente:\t\t"))

hipotenusa = (opuesto**2 + adyacente**2)**(0.5)

print("\nLa medida de la hipotenusa es {:>23.2f}".format(hipotenusa))