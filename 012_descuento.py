precio = float(input("Ingrese el precio del producto\t\t\t\t"))

porc = float(input("\nIngrese el porcentaje de descuento:\t\t\t"))

print("\nEl precio del producto con {} % de descuento es de:{:>9.2f}".format(porc, precio-(precio*(porc/100))))

