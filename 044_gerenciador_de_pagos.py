"""
Escriba un programa que calcule el valor a ser pagado por un producto
considerando el precio normal y l condicion de pago.
- en efectivo (Dinero o cheque) 10 % de decuento
- En efectivo con tarjeta 5 % de descuento
- Dos cuotas en la tarjeta mantiene el precio
- 3 cuotas o mas 20 % de interes
"""

precio_lista = float(input("\33[1;37;40m Ingrese el valor a pagar:\33[m "))

forma_de_pago = int(input("\33[1;37;40m [1] Pago en el acto (Dinero o cheque)\n [2] Pago en el acto (Tarjeta de credito)\n [3] 2 cuotas con tarjeta\n [4] 3 cuotas o mas con tarjeta\nCual es la opción?\33[m  "))

opcion_1 = precio_lista - (precio_lista*0.1)
opcion_2 = precio_lista - (precio_lista*0.05)


if forma_de_pago == 1:
    print("\nSu compra es de R$ {} , y el valor final es de R$ {}".format(precio_lista,opcion_1))
elif forma_de_pago == 2:
    print("\nSu compra es de R$ {} , y el valor final es de R$ {}".format(precio_lista,opcion_2))
elif forma_de_pago == 3:
    print("\nSu compra fue de R$ {} , el valor final es de R$ {} , y cada cuota es de R$ {:.2f}".format(precio_lista,precio_lista,precio_lista/2))
elif forma_de_pago == 4:
    cuotas = int(input("\33[1;37;40m \nIngrese la cantidad de cuotas:\33[m  "))
    opcion_4 = precio_lista + (precio_lista*0.20)
    print("\nSu compra fue de R$ {} , el valor final es de R$ {} , y cada cuota es de R$ {:.2f}".format(precio_lista,opcion_4,opcion_4/cuotas))
else:
    total = 0
    print("Opcion invalida de pago. Intente nuevamente")
    print("Su compra de R$ {} va a costar R$ {}".format(precio_lista,total))