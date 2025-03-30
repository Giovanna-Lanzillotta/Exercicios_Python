# 23. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                           Até 5 Kg                 Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
# adquiridas e escreva o valor a ser pago pelo cliente.


qtd_morangos = float(input("Qual a quantidade em kg de morangos: "))
qtd_macas = float(input("Qual a quantidade em kg de maças: "))

if qtd_morangos < 5:
    preco_morango = qtd_morangos * 2.50
else:
    preco_morango = qtd_morangos * 2.20
    if qtd_morangos > 8 or preco_morango > 25:
        desconto = preco_morango * 0.10
        preco_morango = preco_morango - desconto



if qtd_macas < 5:
    preco_macas = qtd_macas * 1.80
else:
    preco_macas = qtd_macas * 1.50
    if qtd_macas > 8 or preco_macas > 25:
        desconto = preco_macas * 0.10
        preco_macas = preco_macas - desconto

print(f"""
      🍓MORANGOS🍓
 KGS DE MORANGOS: {qtd_morangos}
 PREÇO MORANGOS: R$ {preco_morango}
        🍎MAÇAS🍎
 KGS DE MAÇAS: {qtd_macas}
 PREÇO MAÇAS : R$ {preco_macas}
      """)
