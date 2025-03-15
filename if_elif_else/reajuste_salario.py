#8. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
#desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#baseado no salário atual.
# salários até R$ 280,00(incluindo):aumento de 20%
# salário entre R$ 280,00 e R$ 700,00: aumento de 15%
# salário ente R$ 700,00 e R$ 1500,00: aumento de 10%
# salário de R$ 1500,00 em diante: aumento de 5%
#Após o aumento ser realizado,informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário,após o aumento.

salario = float(input("Digite o salário: "))

if salario <= 280:
    percentual_aumento = 0.20
    aumento = salario * percentual_aumento
    reajuste = salario + aumento
elif salario > 280 and salario < 700:
    percentual_aumento = 0.15
    aumento = salario * percentual_aumento
    reajuste = salario + aumento
elif salario >= 700 and salario < 1500:
    percentual_aumento = 0.10
    aumento = salario * percentual_aumento
    reajuste = salario + aumento
else:
    percentual_aumento = 0.05
    aumento = salario * percentual_aumento
    reajuste = salario + aumento

print(f"""
          💰REAJUSTE DE SALÁRIOS💰
          Salário antes do reajuste: R$ {salario:.2f}
          Percentual de aumento: {percentual_aumento:.2f} %
          Valor do aumento: R$ {aumento:.2f}
          Novo salário: R$ {reajuste:.2f}
          """)