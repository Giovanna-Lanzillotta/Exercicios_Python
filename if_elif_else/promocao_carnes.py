# 24. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                           Até 5 Kg               Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra           R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha          R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
# valor do desconto e valor a pagar.

tipo_carne = int(input(f"""
                       Escolha Apenas um tipo de carne:
                       1 - filé Duplo
                       2 - Alcatra
                       3 - Picanha
                       """))

qtd_carne = int(input(f"Qual a quantidade de carne: "))

# Filé Duplo
if tipo_carne == 1:
    carne = "Filé Duplo"
    if qtd_carne <=5:
       preco =  qtd_carne * 4.90
    else:
      preco =  qtd_carne * 5.80

# Alcatra
if tipo_carne == 2:
    carne = "Alcatra"
    if qtd_carne <=5:
       preco = qtd_carne * 5.90
    else:
       preco = qtd_carne * 6.80

# Picanha
if tipo_carne == 3:
    carne = "Picanha"
    if qtd_carne <=5:
       preco = qtd_carne * 6.90
    else:
       preco = qtd_carne * 7.80


tipo_pagamento = int(input(f"""
                        Qual a forma de pagamento:
                        1 - Cartão Tabajara
                        2 - Dinheiro
                        3 - Cartão Debito
                         """))

if tipo_pagamento == 1:
   pagou = "Cartão Tabajara"
   desconto = preco * 0.05
   valor_final = preco - desconto

elif tipo_pagamento == 2:
    pagou = "Dinheiro"
    desconto = 0
    valor_final = preco

elif tipo_pagamento == 3:
   pagou ="Cartão Debito"
   desconto = 0
   valor_final = preco

print(f"""NOTA FISCAL
      CARNE: {carne}
      QUANTIDADE: {qtd_carne}
      PREÇO SEM DESCONTO: {preco:.2f}
      TIPO DE PAGAMENTO: {pagou}
      VALOR DO DESCONTO: {desconto:.2f}
      VALOR FINAL: {valor_final:.2f}
      """)