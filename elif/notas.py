#Crie um programa em Python que peça a nota do aluno,que deve ser um float entre 0.00 e 10.0

# Se a nota for menor que 6.0, deve exibir a nota F
# Se a nota for de 6.0 até 7.0, deve exibir a nota D
# Se a nota for entre 7.0 e 8.0, deve exibir a nota C
# Se a nota for entre 8.0 e 9.0, deve exibir a nota B

# Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A

nota = float(input("Informe a nota do aluno entre 0.00 e 10.0: "))

if nota > 0.00 and nota <= 10.0:
    if nota < 6:
        print(f"😬 Sua nota {nota:.2f} equivale a F")
    elif nota >= 6 and nota < 7:
        print(f"😐 Sua nota {nota:.2f} equivale a D")
    elif nota >= 7 and nota < 8:
         print(f"😃 Sua nota {nota:.2f} equivale a C")
    elif nota >=8 and nota < 9:
         print(f"😎 Sua nota {nota:.2f} equivale a B")
    else:
         print(f"🥳 Sua nota {nota:.2f} equivale a A")
else:
     print("❌ Nota não reconhecida!")