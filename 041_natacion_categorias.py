"""
Haga un programa que pida la edad de un participante en una prueba de natacion y lo coloque la categoria correspondiente.

hasta 9 años pre-mini
hasta 14 infantil
hasta 19 junior
hasta 25 senior
superior master
"""
from datetime import date

actual = date.today().year

nacimiento = int(input("\t\33[1;32m Ingrese el año de nacimiento (4 digitos):	\33[m"))

edad = actual - nacimiento

print("\n\t\33[1;32m El atleta tiene {} años\33[m".format(edad))

if edad <= 9:
	print("\n\t\33[1;30;42m Categoria PRE-MINI \33[m")
elif edad <= 14:
	print("\n\t\33[1;30;42m Categoria INFANTIL \33[m")
elif edad <= 19:
	print("\n\t\33[1;30;42m Categoria JUNIOR \33[m")
elif edad <= 25:
	print("\n\t\33[1;30;42m Categoria SENIOR \33[m")
elif edad > 25:
	print("\n\t\33[1;30;42m Categoria MASTER \33[m")
else:
	print("\n\t\33[1;30;42m Categoria ERROR \33[m")