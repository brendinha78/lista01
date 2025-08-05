"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit."""
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")