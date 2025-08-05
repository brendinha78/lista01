"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:"""
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))
produto = (2 * num1) * (num2 / 2)
soma = (3 * num1) + num_real
cubo = num_real ** 3
print("O produto do dobro do primeiro com metade do segundo é:", produto)
print("A soma do triplo do primeiro com o terceiro é:", soma)
print("O terceiro número elevado ao cubo é:", cubo)