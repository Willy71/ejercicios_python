'''
cree un programa que pida el inicio y la secuencia de una progresion
aritmetica y muestre los 10 primeros valores
'''

inicio = int(input("\33[1;30;46mIngrese el inicio de la progresion aritmetica:\33[m       "))
secuencia = int(input("\n\33[1;30;46mIngrese el intervalo de la secuencia:\33[m                "))
decimo = inicio + (10 -1) * secuencia
print()

for n in range(inicio, decimo + secuencia, secuencia):
    print("\33[1m{}\33[m ".format(n), end="◄ ")
print("\33[1;30;46mFIN\33[m")
