'''
cree un programa similar al numero 09 pero esta vez usando el bucle for
'''

num = int(input("Ingrese que tabla quiere calcular:     "))

for x in range(1, 11):
    print("{:>5} {:>5} {:>5} {:>5} {:>5}". format(num, "X", x, "=", num*x))