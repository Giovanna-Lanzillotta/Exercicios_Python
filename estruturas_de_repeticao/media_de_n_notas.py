# 24. Faça um programa que calcule e mostre a média aritnética de N notas.

laco = True
total_notas = 0
qtd = 0
while laco:
    nota = float(input("Digite uma nota: "))
    total_notas +=nota
    qtd = qtd+1
    opcao = int(input(f"""
            1 - soma mais um número"
            2 - sair
            :"""))
    if opcao == 2:
        laco = False
        media = total_notas/qtd
print(f"""
       A soma das notas {total_notas}
        Quantidade das notas {qtd}
        A média das notas {media}
      """)