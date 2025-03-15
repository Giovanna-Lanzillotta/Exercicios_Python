# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e 
# a quantidade de números ímpares.

qtd_par = 0
qtd_impar = 0

for numero in range(10):
    numero = int(input("informe um número: "))
    if numero % 2 == 0:
       qtd_par +=1
    else:
        qtd_impar +=1
print(f"""
    Quantidade de números pares: {qtd_par}
    Quantidade de números ímpares: {qtd_impar}
      """)