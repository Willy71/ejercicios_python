"""
escriba un programa para aprobar un prestamo bancario para la compra de una casa. El programa va a preguntar el valor de la casa el salario del comprador y la cantidad de cuotas (años)
Calcule el valor de la cuota sabiendo que no puede exceder el 30% del salario o entonces el prestamo sera negado
"""
valor_casa = float(input("\t\33[1;37;44mIngrese el valor de la propiedad:	\33[m"))

salario = float(input("\n\t\33[1;37;44mIngrese su salario mensual:		\33[m"))

anos = float(input("\n\t\33[1;37;44mIngrese la cantidad de años de pagos:	\33[m"))

valor_cuota = valor_casa / (12 * anos)
porc_salario = (valor_cuota / salario)

if porc_salario < 0.30:
	print("\n\t\t\t\33[1;37;42mCredito otorgado\33[m")
	print("\n\33[1;37;44m	El valor de cada cuota es de:		\33[m{}{:.2f}".format("R$", valor_cuota))
else:
	print("\n\t\33[1;37;41mNO se puede otrorgar el prestamo\33[m")

