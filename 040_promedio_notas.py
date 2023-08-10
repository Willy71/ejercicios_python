"""
Crea un programa que pida 2 notas de un alumno y entregue el promedio de las dos.

promedio abajo de 4 9999 reprobado
promedio entre 5 y 6,9999 recuperatorio
promedio encima de 7 aprobado

"""
nota1 = float(input("\t\33[1;37;44mIngrese su primera nota:	"))

nota2 = float(input("\n\t\33[1;37;44mIngrese su segunda nota:	"))

promedio = (nota1 + nota2)/2

if promedio < 5:
	print("\n\t\t\t\33[1;37;41m Reprobado \33[m")
elif 7 > promedio >= 5:
	print("\n\t\t\t\33[1;37;45m Recuperatorio \33[m")
elif promedio >= 7:
	print("\n\t\t\t\33[1;30;42m Aprobado \33[m")
else:
	print("\n\t\t\t\33[mError")