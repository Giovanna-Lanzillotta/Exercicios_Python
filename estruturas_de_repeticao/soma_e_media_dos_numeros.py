# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

total_numero = 0
for numero in range(5):
    numero = float(input("informe um número: "))
    total_numero += numero
    media = total_numero/5
print(f"""
    A soma dos números é: {total_numero}
    A média dos números é : {media}
        """)