"""
Haga un programa que indique la masa corporal de un usuario
abajo de 18.5 kg (Abajo de su peso)
entre 18.5 y 25 (Peso ideal)
entre 25 y 30 (Sobrepeso)
entre 30 y 40 (Obesidad)
encima de 40 (Obesidad morbida)

imc = peso/altura*altura
"""

peso = float(input("Ingrese su peso en KG:      "))
altura = float(input("Ingrese su altura en mts:     "))
imc = peso / (altura**2)

print("El indice de mas corporal de esa persona es de {:.2f}".format(imc))

if imc < 18.5:
    print("\33[1;37;40m La persona tiene bajo peso \33[m")
elif 18.5 <= imc < 25:
    print("\33[1;37;40m La persona tiene peso ideal \33[m")
elif 25 <= imc < 30:
    print("\33[1;37;40m La persona esta con sobrepeso \33[m")
elif 30 <= imc < 40:
    print("\33[1;37;40m La persona tiene obesidad \33[m")
else:
    print("\33[1;37;40m La persona tiene obesidad morbida \33[m")


