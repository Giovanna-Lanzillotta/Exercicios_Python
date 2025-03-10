#3. Faça um programa que leia três números imteiros e mostre p maior deles.

numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))
numero_3 = int(input("Digite o terceiro número inteiro: "))

if numero_1 > numero_2 and numero_1 >numero_3:
    print(f"O {numero_1} é maior que o {numero_2} e o {numero_3}")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"O {numero_2} é maior que o {numero_1} e o {numero_3}")
else:
    print(f"O {numero_3} é maior que o {numero_1} e o {numero_2}")