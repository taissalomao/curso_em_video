# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input("Qual o valor do salário? "))

aumento = (salario * 15) / 100

salarioComAumento = salario + aumento

print(f'Seu novo salário com aumento é R$ {salarioComAumento}')

