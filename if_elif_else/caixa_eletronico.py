# 18. Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor
# serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: 
# Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, 
# uma nota de 5 e uma nota de 1;
# Exemplo 2: 
# Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
# quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = float(input("Qual o valor do saque: "))

if valor_saque < 10 or valor_saque > 600:
    print("O SAQUE PRECISA SER ENTRE 10 E 600!")
else:
    valor_cem = int(valor_saque/100)
    valor_saque = (valor_saque % 100)
    
    valor_cinquenta = int(valor_saque/50)
    valor_saque = (valor_saque % 50)

    valor_dez = int(valor_saque/10)
    valor_saque = (valor_saque % 10)

    valor_cinco = int(valor_saque/5)
    valor_saque = (valor_saque % 5)

    valor_um = int(valor_saque)

    print(f"""
      💰 SAQUE 💰
      NOTAS DE 1 : {valor_um}
      NOTAS DE 5 : {valor_cinco}
      NOTAS DE 10 : {valor_dez}
      NOTAS DE 50 : {valor_cinquenta}
      NOTAS DE 100 : {valor_cem}
      """)

