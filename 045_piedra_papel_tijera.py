'''
Cree un programa para jugar piedra papel y tijera
'''

from random import randint
from time import sleep

computadora = randint(0,2)
items = ("Piedra", "Papel", "Tijera")
print("Sus opciones: ")
print("[0] Piedra\n[1] Papel \n[2] Tijera")
jugador = int(input("Elija una de las tres opciones:     "))
sleep(1)
print("Piedra")
sleep(1)
print("Papel")
sleep(1)
print("O Tijera!!!!")
sleep(1)
print("-=" * 11)
print("La computadora eligio {}".format(items[computadora]))
print("Usted eligio {}".format(items[jugador]))
print("-=" * 11)
if computadora == 0: #Computadora eligio piedra
    if jugador == 0: # piedra
        print("Esta partida fue empate")
    elif jugador == 1: #papel
        print("Usted gano este juego!!")
    elif jugador == 2: #tijera
        print("La computadora gano este juego")
    else:
        print("Coloco una opcion errada. Vuelva a intentar mas tarde")
elif computadora == 1: #Computadora eligio papel
    if jugador == 0: #piedra
        print("La computadora gano este juego!!!")
    elif jugador == 1: #papel
        print("Esta partida fue empate")
    elif jugador == 2: #tijera
        print("Usted gano este juego!!")
    else:
        print("Coloco una opcion errada. Vuelva a intentar mas tarde")
elif computadora == 2: #Computadora eligio tijera
    if jugador == 0: #Piedra
        print("Usted gano este juego!!")
    elif jugador == 1: #papel
        print("La computadora gano este juego!!!")
    elif jugador == 2: #Tijera
        print("Esta partida fue empate")
    else:
        print("Coloco una opcion errada. Vuelva a intentar mas tarde")


