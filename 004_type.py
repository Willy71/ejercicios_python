x = input("Ingrese algun dato:\t\t")

n = type(x)
print("\n{} es una entrada de tipo \t{}".format(x, n))

print("\nPuede ser un numero entero?\t{}".format(x.isnumeric()))

print("\nEs un dato solo con espacios?\t{}".format(x.isspace()))

print("\nEs un dato alfanumerico?\t{}".format(x.isalnum()))

print("\nEs un dato alfabetico?\t\t{}".format(x.isalpha()))

print("\nEs un dato en mayusculas?\t{}".format(x.isupper()))

print("\nEs un dato en minusculas?\t{}".format(x.islower()))

print("\nEs un dato capitalizado?P\t{}".format(x.istitle()))

#como hacer para mostrar x decimales en los resultados {:.xf}
a = 34
b = 7
d = a/b
print("\nLa division de {} por {} es\t{:.2f}".format(a,b,d), end=" ")
print("consegui colocar solo dos digitos")

