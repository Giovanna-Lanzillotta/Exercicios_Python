# 5. Faça um programa que pede dois inteiro e armazene em duas variáveis. 
# Em seguida, troque o valor das variáveis e exiba na tela

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
 
aux = numero2
numero2 = numero1
numero1 = aux


print(f"""
    Números trocados : {numero1} e { numero2}
      """)

