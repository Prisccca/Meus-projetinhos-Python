# Faça um programa que receba o salário base de um funcionário 
# calcule e mostre o seu salario a receber 
# sabendo-se que o funcionario tem gratificação de R$ 50
# paga imposto de 10% sobre o salário base 

sal = float(input("Digite o salário do funcionário: "))
imp = sal * 0.1
salReceber = sal + 50 - imp
print("Salário a receber: R$", salReceber)