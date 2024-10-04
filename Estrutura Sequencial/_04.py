# Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%

sal = int(input("Digite o salário do funcionário: "))
novosal = sal + (sal * 0.25)
print("O salario atualizado é: R$", novosal)