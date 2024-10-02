#Faça um programa que receba 3 notas, calcule e mostre a média aritmetica entre elas.

print("Calculadora de Médias")
x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))
z = float(input("Digite a terceira nota: "))

soma = x + y  + z 
media = soma/3
print("A média é " ,round(media))