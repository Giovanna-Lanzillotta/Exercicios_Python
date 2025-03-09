#3. Sua primeira tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.

#Você deve mostrar um tabela contento:
#Preço original do produto
#Valor do desconto wm R$ (tipo você ganhou R$ xx,xx de desconto)
# valor do produto

preco_original = float(input("Informe o preço original do produto: "))

desconto = preco_original * 0.20
preco_desconto = preco_original - desconto

print(f"""
     💰 TABELA DE DESCONTO DE 20% 💰
-----------------------------------------------
Preço Original R$: {preco_original:.2f}
Valor do Desconto R$: {desconto:.2f}
Preço final com desconto R$: {preco_desconto:.2f}
------------------------------------------------
      """)