# 10. Faça um programa que leia um número e exiba o dia correspondente sa semana:
# (1 - Domingo,2 - Segunda, etc),se digitar outro valor deve aparecer valor inválido.

dia_semana = int(input(f"Insira um dia da semana de 1 a 7: "))

if dia_semana == 1 :
    print("🐱‍👓DOMINGO")
elif dia_semana == 2:
    print("🐱‍💻SEGUNDA")
elif dia_semana == 3:
    print("🐱‍💻TERÇA")
elif dia_semana == 4:
    print("🐱‍💻QUARTA")
elif dia_semana == 5:
    print("🐱‍💻QUINTA")
elif dia_semana == 6:
    print("🐱‍💻SEXTA")
elif dia_semana == 7:
    print("🐱‍👓SABÁDO")
else:
    print("❌ Valor inválido")
