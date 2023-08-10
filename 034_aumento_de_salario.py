salario = float(input("Ingrese su salario:\t"))

if salario <= 1250:
	print("\nEl nuevo salario es de R$ {}".format(salario+(salario*.10)))
else:
	print("\nEl nuevo salario es de R$ {}".format(salario+(salario*.15)))