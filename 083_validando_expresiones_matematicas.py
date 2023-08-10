'''
cree un programa en donde el usuario digite una expresion matematica cualquiera
que use parentesis. Su app debera analisar esa expresion pasada esta con los
parentesis abiertos o cerrados en el orden correcto
'''

expresion = ''
lista = []

expresion = str(input('Ingrese una expresion matematica con párentesis:     '))
pila = []

for simb in expresion:
    if simb == '(':
        pila.append('(')
    elif simb == ')':
        if len(pila) > 0:
            pila.pop()
        else:
            pila.append(')')
            break
if len(pila) == 0:
    print('Su expresion matematica es valida')
else:
    print('Su expresion matematica NO es valida')




'''
for n in expresion:
    lista.append(n)
num_uno = lista.index(')')
num_dos = lista.index('(')
if lista.count('(') == lista.count(')') and num_uno > num_dos:
    print('Su expresion matematica es valida')
else:
    print("Su expresion matematica no es valida")
'''


