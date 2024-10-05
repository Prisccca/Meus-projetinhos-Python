# Faça um programa que receba o salario base de um funcionário
# calcule e mostre o salario a receber 
# sabendo-se que o funcionario tem gratificação de 5% sobre o salario base
# paga imposto de 7% sobre este salario

sal = float(input("Digite o salário do funcionário: "))
grat = sal * 0.05
imp = sal * 0.07
salReceber = sal + grat -imp

print("Salário a receber: R$", salReceber)
