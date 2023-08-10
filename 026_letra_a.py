"""
haga un programa que diga:
1- cuantas veces aparece la letra A.
2- cuando aparece por primera vez
3- cuando aparece por ultima vez
"""

frase = str(input("Ingrese una frase:\t")).strip()

print("\nLa letra A aparece {} cantidad de veces".format(frase.lower().count("a")))

print("\nLa letra A aparece por primera vez en la {} posicion".format(frase.lower().find("a")+1))

print("\nLa letra A aparece por ultima vez en la {} posicion".format(frase.lower().rfind("a")+1))

