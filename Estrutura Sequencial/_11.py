# Faça um programa que receba um numero positivo e maior que zero, calcule e mostre:
# a) o numero digitado ao quadrado
# b) o numero digitado ao cubo
# c) a raiz quadrada do numero digitado 
# d) a raiz cúbica do número digitado

import math
from math import cbrt


num = float(input("Digite um número positivo e maior que zero: "))

quad = math.pow(num,2)
cubo = math.pow(num,3)
r2 = math.sqrt(num)
r3 = math.cbrt(num)

print("Numero ao quadrado: ",quad)
print("Numero ao cubo: ",cubo)
print("Raiz quadrada do numero: ",r2)
print("Raiz cubica do numero: ",r3)
