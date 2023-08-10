'''
Haga un programa que haga una cuenta regresiva para el lanzamiento de fuegos de
artificio de 10 a 0, con una pasusa de un segundo entre uno y otro
'''

from time import sleep

for c in range (10, -1, -1):
    sleep(1)
    print(c)
print("Que comienzen los fuegos artificiales!!!!")