# 32.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120


numero = int(input("Digite um número inteiro: "))


i = 0
fatorial = 1

for i in range(1,numero + 1):

    fatorial *= i
    
    
print(f"""
          O fatorial do {numero} é {fatorial} """)