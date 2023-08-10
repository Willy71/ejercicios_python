nome = str(input("Ingrese su nombre y apellido:\t\t")).strip()

print("\nSu nombre en minusculas es:{:^40}".format(nome.lower()))

print("\nSu nombre en mayusculas es:{:^40}".format(nome.upper()))

print("\nLa cantidad de letras sin espacios es:{:^30}".format(len(nome) - nome.count(" ")))

#print("\nLa cantidad de letras del primer nombre es:{:^20}".format(nome.find(" ")))

separa = nome.split()

print("\nLa cantidad de letras de {} es:{:^30}".format(separa[0], len(separa[0])))

