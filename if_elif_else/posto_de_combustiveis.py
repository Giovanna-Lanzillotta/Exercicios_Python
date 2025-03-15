# 22 . Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro. Acima de 20 litros, desconto de 5% por litro.
# Gasolina: até 20 litros, desconto de 4% por litro. Acima de 20 litros, desconto de 6 % por litro.
# Escreva um algoritmo que leia o número de litros vendidos,o tipo de combustível(codificado da seguinte forma:
# A - Álcool,G - Gasolina),calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
# de gasolina é R$ 2,50, o preço do litro do álcool é R$ 1,90.

combustivel = input(f"""
                    Qual o tipo de combustível
                    A - Álcool
                    G - Gasolina
                    : """)

litros = float(input("Quantos litros deseja colocar: "))

if combustivel == "A":
    tipo = "álcool"
    litro_fixo = 1.90
    if litros <= 20:
        preco = litro_fixo * litros
        desconto = litros * 0.03
        total = preco + desconto
    elif litros > 20:
        preco = litro_fixo * litros
        desconto = litros * 0.05
        total = preco + desconto

elif combustivel == "G":
    tipo = "gasolina"
    litro_fixo = 2.50
    if litros <= 20:
        preco = litro_fixo * litros
        desconto = litros * 0.04
        total = preco + desconto
    elif litros > 20:
        preco = litro_fixo * litros
        desconto = litros * 0.06
        total = preco + desconto

print(f"""
      Você colocou {litros:.2f} litros 
      de {tipo}
      dando um desconto de R$ {desconto:.2f}
      você irá pagar R$ {total:.2f}
      """) 


