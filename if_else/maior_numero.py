# 1. Faça um programa que peça dois números e imprima o maior deles.

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro número: "))

if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

print(f"""
Entre os números {numero1} e {numero2}
O maior deles é o {maior}
      """)