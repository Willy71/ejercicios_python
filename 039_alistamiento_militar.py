"""
programa para saber cuanto tiempo falta para el servicio militar

"""
ano = int(input("\t\33[1;37;45mIngrese el año de su nacimiento (4 digitos):	"))

edade = 2023 - ano
diferencia = edade - 18

print("\n\t\33[1;37;45mSu edad es de {} años\33[m".format(edade))

if diferencia > 0:
	print("\n\t\33[1;37;45mPasaron\33[m {} años \33[1;37;45mde su alistamiento\33[m".format(diferencia))
elif diferencia < 0:
	print("\n\t\33[1;37;45mFaltan\33[m {} años \33[1;37;45mpara su alistamiento\33[m".format(diferencia*(-1)))
elif diferencia == 0:
	print("\n\t\33[1;30;42mTiene que alistarse inmediatamente!!!\33[m")
else:
	print("\33[1;37;41Error\33[m")