'''
Cree un programa que lea varios numeros enteros
El programa va a parar cuando el usuario digite el numero 999
Al final muestre cuantos numeros fueron ingresados
y la suma entre ellos (No considere el flag)
'''
resultado = cont = 0

while True:
    usuario = int(input('Ingrese un numero entero [Para salir digite 999]       '))
    if usuario == 999:
        break
    resultado += usuario
    cont += 1
print(f'Usted ingreso {cont} y la suma de ellos fue {resultado}')



