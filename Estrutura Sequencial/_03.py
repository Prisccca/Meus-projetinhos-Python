#Faça um programa que receba 3 notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas

print("Calculadora de Médias Ponderadas: ")
x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))
z = float(input("Digite a terceira nota: "))

a = float(input("Digite o peso da primeira nota: "))
b = float(input("Digite o peso da segunda nota: "))
c = float(input("Digite o peso da terceira nota: "))

nota1 = x * a
nota2 = y * b
nota3 = z * c

media = (nota1 + nota2 + nota3) / (a + b + c)

print("A média final é: ", media)