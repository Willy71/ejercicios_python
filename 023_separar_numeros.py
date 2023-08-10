"""
haga un programa que pida un numero entre 100 y 9999 y separe los numeros

"""
numero = int(input("Ingrese un numero entre 0 y 9999:\t\t"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("\nLa unidad de {} es: {:>30}".format(numero, u))
print("\nLa decena de {} es: {:>30}".format(numero, d))
print("\nLa centena de {} es: {:>29}".format(numero, c))
print("\nLa unidad de mil de {} es: {:>23}".format(numero, m))
