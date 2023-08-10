"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

dias = int(input("Ingrese la cantidad de dias de alquiler del vehículo:\t\t"))

kms = float(input("\nIngrese la cantidad de kilometros recorridos:\t\t\t"))

total = (dias*60)+(kms*0.15)

print("\nEl precio total a pagar es de:{:>32} {}".format("R$", total))