salario = float(input("Ingrese el valor de su salario:\t\t\t\t"))

porc_aum = float(input("\nIngrese el porcentaje de aumento:\t\t\t"))

print("\nEl nuevo salario con {} % de aumento es de:{:>18.2f}".format(porc_aum, salario+(salario*(porc_aum/100))))

