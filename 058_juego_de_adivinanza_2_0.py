'''
Cree un programa de adivinanza donde la computadora va a 'Pensar'
un numero entre 0 y 10, solo que ahora el usuario va a intentar hasta
acertar, mostrando al final cuantos intentos uso para acertar.
'''

from random import randint

numero = randint(0, 10)
contador = 0
print('Hola, soy su computadora...\nAcabe de pensar un número del 0 al 10.\nSerá que consigue adivinar que numero es?')

acerto = False
usuario = int(input('Cual es su palpito?....                            '))

while not acerto:
    contador += 1
    if usuario == numero:
        acerto = True
    elif usuario > numero:
        usuario = int(input('Su número es mayor. Intente nuevamente             '))
    elif usuario < numero:
        usuario = int(input('Su numero es menor. Intente nuevamente             '))
print('Acerto en el {} intento'.format(contador))
