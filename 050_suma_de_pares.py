'''
Cree un programa que lea seis numeros enteros
y muestre la suma solo de aquellos numeros que sean pares
Si el valor colocado es impar, descartelo
'''
suma = 0
cont = 0
for n in range(1, 7):
    num = int(input("Digite el {} valor:      ".format(n)))
    if num % 2 == 0:
        suma += num
        cont += 1
print("\nLa suma de los {} numeros\npares que usted ingreso es:       {}".format(cont, suma))