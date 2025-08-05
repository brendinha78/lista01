"""
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em """

area = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))
cobertura_por_litro = 6
litros_necessarios = area / cobertura_por_litro
litros_necessarios *= 1.1
litros_necessarios = math.ceil(litros_necessarios)
litros_lata = 18
preco_lata = 80.00

litros_galao = 3.6
preco_galao = 25.00

latas_necessarias = math.ceil(litros_necessarios / litros_lata)
preco_latas = latas_necessarias * preco_lata

galoes_necessarios = math.ceil(litros_necessarios / litros_galao)
preco_galoes = galoes_necessarios * preco_galao

latas_mistas = math.floor(litros_necessarios / litros_lata)
litros_restantes = litros_necessarios - (latas_mistas * litros_lata)
galoes_mistos = math.ceil(litros_restantes / litros_galao)
preco_misto = (latas_mistas * preco_lata) + (galoes_mistos * preco_galao)

print("\n--- Opções de Compra ---")
print(f"1. Apenas latas de 18L: {latas_necessarias} lata(s) - Preço: R$ {preco_latas:.2f}")
print(f"2. Apenas galões de 3,6L: {galoes_necessarios} galão(ões) - Preço: R$ {preco_galoes:.2f}")
print(f"3. Mistura: {latas_mistas} lata(s) e {galoes_mistos} galão(ões) - Preço: R$ {preco_misto:.2f}")