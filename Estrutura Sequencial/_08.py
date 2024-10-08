# Faça um programa que receba o valor de um depósito e o valor da taxa de juros
# calcule e mostre  o valor do rendimento e o valor total depois do rendimento

dep = float(input("Digite o valor do deposito: "))
taxa = float(input("Digite a taxa de juros: "))

rend = dep * (taxa/100)
total = dep + rend

print("O valor do Rendimento: ",rend)
print("O valor total é: ",total)