'''
cree un programa que lea un numero y diga si ese numero
es numero primo
'''
cont = 0

numero = int(input("\33[1;30;44mIngrese un número entero:\33[m       "))

for m in range(1, numero + 1):
    if numero%m == 0:
        cont += 1

if cont > 2:
    print("\n       \33[1;30;41mNo es numero primo\33[m")
else:
    print("\n       \33[1;30;42mEs numero primo\33[m")
