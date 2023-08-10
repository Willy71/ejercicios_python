"""
cree un programa que pida un número float y entregue un numero entero
"""
import math

num = float(input("Ingrese un número con decimales:\t\t"))

entero = math.floor(num)

print("\nEl número entero de {} es:{:>20}".format(num, entero))