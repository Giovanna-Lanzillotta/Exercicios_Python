# 3. Faça um programa que leia 4 notas,mostre as notas e a média na tela.


totalNotas = 0

for nota in range(4):
    notas = [10, 9, 8.6, 6,5]
    totalNotas = sum(notas)
    
    print(f"""
    As notas são {notas}
    A média das notas é {(totalNotas/4):.2f}
""")
