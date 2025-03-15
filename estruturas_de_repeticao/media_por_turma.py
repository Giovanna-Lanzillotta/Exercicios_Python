# 27. Faça um programa que calcule o número médio de alunos por turma.Para isto, peça a quantidade de turmas
# e a quantidade de alunos para cada turma.As turmas não podem ter mais de 40 alunos.

turma = int(input("Qual a quantidade de turmas? "))
total_alunos = 0
for alunos in range(turma):
    alunos = int(input("Qual a quantidade de alunos? "))
    if alunos < 40:
        total_alunos +=alunos
        media = total_alunos/turma
    else:
        print("Quantidade não pode ser superior a 40 alunos!")
        break

print(f"""
    A média de alunos por turma  é {media:.2f}
        """)
