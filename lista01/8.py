"""Faça um Programa que pergunte quanto você ganha 
por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês."""
 
valor_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas você trabalhou no mês? "))
salario = valor_hora * horas_mes
print(f"Seu salário é: R${salario:.2f}")

