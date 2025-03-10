#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.

laco = True

while laco :
    nota = int(input("Digite uma nota de 0 a 10: "))
    if nota >= 0 and nota <= 10:
        print(f"✅ A nota digitada foi {nota}")
        laco = False
    else:
        print("❌ Tente novamente!")


