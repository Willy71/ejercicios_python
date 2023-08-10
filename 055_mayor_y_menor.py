'''
cree un programa que pida 5 pesos de personas
y diga cual es que menos pesa y cual el que mas
'''

mayor = 0
menor = 0

for m in range(1, 6):
    peso = float(input("\33[1;30;44mIngrese el peso del {} participante:\33[m    ".format(m)))
    if m == 1:
        mayor = peso
        menor = peso
    else:
        if peso > mayor:
            mayor = peso
        elif peso < menor:
            menor = peso

print('\n\33[1;30;42mEl mayor peso entre los 5 participantes es de {} Kg\33[m'.format(mayor))
print('\33[1;30;41mEl menor peso entre los 5 participantes es de {} Kg\33[m'.format(menor))
