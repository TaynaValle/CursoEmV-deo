"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

"""
"""from math import trunc"""
import math
num = float(input("Digite um número qualquer: "))
porcaointeira = math.trunc(num)
print("A porção inteira de {} é {}.".format(num, porcaointeira))