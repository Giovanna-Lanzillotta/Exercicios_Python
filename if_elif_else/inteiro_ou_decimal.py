# 19.Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#  Dica: utilize uma função de arredondamento.

numero = float(input("Informe um número: "))

arredonda = round(numero)

if numero == arredonda:
    print("Número Inteiro")
else:
    print("Número Decimal")