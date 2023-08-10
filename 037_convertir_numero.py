""" 
escriba un programa que pida un numero entero y lo convierta en
1- binario
2-octal 
3-hexadecimal
"""

numero = int(input("\t\33[1;37;44mIngrese un número entero:		\33[m"))

opcion = int(input("\n\n\t\33[1;37;44mIngrese una opcion:	\n\n\tOpcion		1		Binario\n\n\tOpcion		2		Octal\n\n\tOpcion		3		Hexadecimal\n\n\t\t\t"))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if opcion == 1:
	print("\n\t\33[1;37;44mEl numero binario de {} es:\33[m		{}".format(numero, binario))
elif opcion == 2:
	print("\n\t\33[1;37;44mEl numero octal de {} es:\33[m		{}".format(numero, octal))
elif opcion == 3:
	print("\n\t\33[1;37;44mEl numero hexadecimal de {} es:\33[m		{}".format(numero, hexadecimal))
else:
	print("\n\33[1;37;44mOpcion invalida, intente nuevamente:\33[m		")