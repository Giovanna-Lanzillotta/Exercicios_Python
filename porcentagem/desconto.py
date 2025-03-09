# A loja percebeu que não quer dar 20% em tudo.Quer dar 20% em algumas coisas, 10% em outras. nada em outro produto 
# e ate 30% em alguns produtos.
#Crie um script em Python que pergumte o preço original e o descontoque deve ser concedido.
# Ele deve mostarar a tabela iguala do exercicio anterior.

preco_original = float(input("Informe o valor original: "))

desconto = float(input("Informe o valor do desconto:\n 10% 20% 30% - nenhum(0%): "))

if desconto == 10:
    preco_desconto = (preco_original * 0.10)
    preco_final = preco_original - desconto
elif desconto == 20:
    preco_desconto = (preco_original * 0.20)
    preco_final = preco_original - desconto
elif desconto == 30:
    preco_desconto = (preco_original * 0.30)
    preco_final = preco_original - desconto
else:
    preco_final = preco_original 
    desconto = 0

print(f"""
         💰 TABELA DE DESCONTO DE 20% 💰
    -----------------------------------------------
    Preço Original R$: {preco_original:.2f}
    Valor do Desconto R$: {desconto:.2f}
    Preço final com desconto R$: {preco_final:.2f}
    ------------------------------------------------
          """)

