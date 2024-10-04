# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário

sal = float(input("Digite o salário do funcionário: "))
perc = float(input("Digite a porcentagem de aumento: "))

aumento = sal * (perc/100)
novosal = sal + aumento

print("Valor do aumento:", round(aumento))
print("Salário Atualizado: R$",round(novosal))