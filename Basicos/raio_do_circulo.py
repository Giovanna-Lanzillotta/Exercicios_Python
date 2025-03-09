# 01 . Escreva um programa que pede o raio de um círculo, e em seguida exiba o perímetro e área do c´rculo.
# Para saber o valor de pi,faça:
# import math
# print(math.pi)
# Pronto, para saber valor de pi, bastar usar 'math.pi' que é um float

import math

raio = float(input("🔴Digite o raio do círculo: "))

perimetro = 2*raio*(math.pi)
area = (math.pi)*(raio)**2

print(f"O perimetro do círculo é: {perimetro:.2f}")
print(f"A área do círculo é: {area:.2f}")
