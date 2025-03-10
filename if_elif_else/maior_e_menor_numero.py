# 4. Faça um programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))
numero_3 = int(input("Digite o terceiro número inteiro: "))

#Maior número
if numero_1 > numero_2 and numero_1 >numero_3:
    maior = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
else:
    maior = numero_3

#Menor número
if numero_1 < numero_2 and numero_1 < numero_3:
    menor = numero_1
elif numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
else:
    menor = numero_3

print(f"""
    Os números digitados são: {numero_1}, {numero_2}, {numero_3}
    O maior número é {maior}
    O menor número é {menor}
      """)
