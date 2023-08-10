'''
Cree un programa que juegue par o impar con la computadora.
El juego sera interrumpido cuando el usuario pierda, mostrando
el total de victorias que el usuario conquisto al final del juego.
'''

from random import randint

print('=-='*19)
print("\33[1;30;44m                Vamos a jugar par o impar                \33[m")
print('=-='*19)

azar = resultado = cont = 0
par_impar = pi_res = pires = parimpar = ""


while True:
    numero = int(input('Ingrese un número entero del 1 al 9:        '))
    azar = randint(1, 9)
    par_impar = str(input('Ingrese Par o Impar [P/I]:                  ')).strip().upper()[0]
    print('=-='*19)
    resultado = numero + azar
    if resultado % 2 == 0:
        pi_res = "P"
        pires = "par"
    else:
        pi_res = "I"
        pires = "impar"

    if par_impar == "P":
        parimpar = "par"
    else:
        parimpar = "impar"

    if pi_res == par_impar:
        cont += 1
        print(f'Usted digito {numero} y la computadora {azar}. Total {resultado}, o sea {pires}')
        print(f'Como usted tambien dijo {parimpar} gano esta partida')
        print('=-='*19)
    else:
        print(f'Usted digito {numero} y la computadora {azar}. Total {resultado}, o sea {pires}')
        print(f'Como usted dijo {parimpar} perdio esta partida')
        print(f'Juego terminado!!!! Gano {cont} veces')
        break