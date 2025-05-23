# 9. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do 
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#     Salário Bruto: (5 * 220)        : R$ 1100,00
#     (-) IR (5%)                     : R$   55,00 
#     (-) INSS ( 10%)                 : R$  110,00
#     FGTS (11%)                      : R$  121,00
#     Total de descontos              : R$  165,00
#     Salário Liquido                 : R$  935,00


valor_hora = float(input("Qual o valor da sua hora: "))

qtd_horas_trabalhadas = float(input("Quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * qtd_horas_trabalhadas


# Salário Bruto até 900 (inclusive) - isento
if salario_bruto <= 900:
    print("Isento")

#  Salário Bruto até 1500 (inclusive) - desconto de 5%
elif salario_bruto <= 1500:
    desconto = (salario_bruto * 0.05)
    ir = (salario_bruto * 0.05)
    inss = (salario_bruto * 0.1)
    fgts = (salario_bruto * 0.11)
    total_desconto = ir + inss
    salario_liquido = (salario_bruto - total_desconto)

    print(f"""
        DESCONTO DO IR
        SALÁRIO BRUTO R$ {salario_bruto:.2f}
        (-)IR R$ {ir:.2f}
        (-)INSS R$ {inss:.2f}
        FGTS R$ {fgts:.2f}
        TOTAL DE DESCONTOS R$ {total_desconto:.2f}
        SALÁRIO LIQUIDO R$ {salario_liquido:.2f}
      """)

# Salário Bruto até 2500 (inclusive) - desconto de 10%
elif salario_bruto <= 2500:
    desconto = (salario_bruto * 0.10)
    ir = (salario_bruto * 0.05)
    inss = (salario_bruto * 0.1)
    fgts = (salario_bruto * 0.11)
    total_desconto = ir + inss
    salario_liquido = (salario_bruto - total_desconto)

    print(f"""
        DESCONTO DO IR
        SALÁRIO BRUTO R$ {salario_bruto:.2f}
        (-)IR R$ {ir:.2f}
        (-)INSS R$ {inss:.2f}
        FGTS R$ {fgts:.2f}
        TOTAL DE DESCONTOS R$ {total_desconto:.2f}
        SALÁRIO LIQUIDO R$ {salario_liquido:.2f}
      """)

# Salário Bruto acima de 2500 - desconto de 20%
elif salario_bruto > 2500:
    desconto = (salario_bruto * 0.10)
    ir = (salario_bruto * 0.05)
    inss = (salario_bruto * 0.1)
    fgts = (salario_bruto * 0.11)
    total_desconto = ir + inss
    salario_liquido = (salario_bruto - total_desconto)

    print(f"""
        DESCONTO DO IR
        SALÁRIO BRUTO R$ {salario_bruto:.2f}
        (-)IR R$ {ir:.2f}
        (-)INSS R$ {inss:.2f}
        FGTS R$ {fgts:.2f}
        TOTAL DE DESCONTOS R$ {total_desconto:.2f}
        SALÁRIO LIQUIDO R$ {salario_liquido:.2f}
      """)