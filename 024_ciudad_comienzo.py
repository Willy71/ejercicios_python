""" 
coloque el nombre de una ciudad y diga si comienza con la palabra Santo
"""
ciudad = str(input("Ingrese la ciudad en donde nacio:\t")).strip()

val = ciudad[:5].lower() == "santo"

print("\nLa ciudad en donde usted nacio comienza con la palabra Santo: {}".format(val))

