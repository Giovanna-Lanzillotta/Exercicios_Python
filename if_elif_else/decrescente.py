# 6. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
numero3 = float(input("Digite mais um número: "))

# Maior número
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
else:
    maior = numero3

# Menor número
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
else:
    menor = numero3


if numero1 < maior and numero1 > menor:
    meio = numero1
if numero2 < maior and numero2 > menor:
    meio = numero2
if numero3 < maior and numero3 > menor:
    meio = numero3

print(f"ordem decrescente {maior} > {meio} > {menor}")

