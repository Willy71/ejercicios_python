	"""
escriba un programa que lea dos números y díga cuál es mayor y cuál es menor

"""

num1 = int(input("\t\33[1;37;41mIngrese un número entero:		\33[m"))

num2 = int(input("\n\t\33[1;37;41mIngrese un número entero:		\33[m"))

if num1 > num2:
	print("\n\t\33[1;37;41mEl primer número es mayor que el segundo.\33[m".format(num1, num2))
elif num2 > num1:
	print("\n\t\33[1;37;41mEl segundo número es mayor que el primero.\33[m".format(num2, num1))
else:
	print("\n\t\33[1;37;44mLos números son iguales.\33[m")
	