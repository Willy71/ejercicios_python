'''
Cree un programa que tenga una tupla con varias palabras
(No usar acentos) . Despues de eso usted debe mostrar cuales son las
palabras y sus vocales
'''

palabras = ("Aprender", 'Programar', 'Lenguaje', 'Programacion', 'Python', 'Curso', 'Gratis', 'Estudiar', 'Practicar', 'Trabajar', 'Mercado', 'Programador', 'Futuro')

for n in palabras:
    print(f'\nEn la palabra \33[1;33m{n.upper():<2}\33[m tenemos ', end = '')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(f'\33[1;33m{letra.lower()}\33[m', end = ' ')