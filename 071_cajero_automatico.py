'''
Cree un programa  que simule el funcionamiento de un cajero automatico.
Al inicio que pregunte al usuario que valor desea sacar (numero entero)
El programa va a informar cuantos billetes de cada valor va a entregar.
Considere que el cajero tiene billetes de 50, 20, 10. 5, 1
'''
cincuenta = veinte = diez = uno = 0
resto_50 = resto_20 = resto_10 = resto_1 = 0

print('=-'*35)
print('\33[1;30;44m                     Bienvenido a la Red Banelco                      \33[m')
print('=-'*35)

while True:
    valor = int(input('Informe el valor que desea sacar (Numero entero)         '))
    print('=-'*35)
    cincuenta = valor // 50
    resto_50 = valor % 50
    veinte = resto_50 // 20
    resto_20 = resto_50 % 20
    diez = resto_20 // 10
    resto_10 = resto_20 % 10
    uno = resto_10 // 1
    print('Se entregaran:')
    if cincuenta >0:
        print(f"               {cincuenta} billetes de R$ 50")
    if veinte > 0:
        print(f"               {veinte} billetes de R$ 20")
    if diez > 0:
        print(f'               {diez} billetes de R$ 10')
    if uno > 0:
        print(f'               {uno} billetes de R$ 1')

    continuar = " "
    while continuar not in 'SN':
        print('=-'*35)
        continuar = str(input('Desea continuar? [S/N]       ')).strip().upper()[0]
        print('=-'*35)
    if continuar == 'N':
        print('\33[1;30;44m      Vuelva siempre al Banco de Galicia!! Que tenga un buen dia      \33[m')
        print('=-'*35)
        break


