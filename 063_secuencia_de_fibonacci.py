'''
Cree un programa que le pida al usuario
cuantos resultados desea ver de la secuencia de fibonacci
comenzando de 0
'''

proximo = 1
anterior = 0
resultado = 0
cont = 0
print('='*70)
print('\33[1;30;44m                       Secuencia de Fibonacci                         \33[m')
print('='*70)
cantidad = int(input('Cuantos resultados de la secuencia de Fibonacci desea ver?        '))
print('='*70)

while cont < cantidad:
    resultado = proximo
    proximo = anterior
    anterior += resultado
    cont += 1
    print('►', proximo, end = " ")
print()
print('='*70)