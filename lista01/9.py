"""Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)."""

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (5 * (fahrenheit - 32)) / 9
print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius:.2f} graus Celsius.")
 