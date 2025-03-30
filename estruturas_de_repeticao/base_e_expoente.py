# 13.Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado 
# ao segundo número. 
# Não utilize a função de potência da linguagem.

expoente = float(input("Digite o expoente: "))
base =  float(input("Digite a base: ")) 

resultado = base**expoente

print(f"""
      O expoente: {expoente}
      A base: {base}
      O resultado: {resultado}
      """)