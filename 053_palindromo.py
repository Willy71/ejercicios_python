'''
cree un programa que lea una frase y diga si esa frase es un palindromo
sin considerar los espacios

palindromo: Dicese de la frase o palabra que se puede ler de la misma manera al derecho o
al reves
'''

lista = []
lista_2 = []

frase = str(input("\33[1;37;40mIngrese una frase o palabra:\33[m ")).strip().upper()
palabras = frase.split()
junto = ''.join(palabras)
invertir = junto[::-1]

'''
for letra in range(len(junto)-1,-1,-1):
    invertir += junto[letra]
'''
print('\nLa frase inversa de "{}" es "{}"'.format(junto, invertir))

if junto == invertir:
    print("\n\33[1;30;42mEs un palindromo\33[m")
else:
    print("\n\33[1;30;41mNo es un palindromo\33[m")


