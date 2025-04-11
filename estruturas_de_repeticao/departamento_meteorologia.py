# 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as 
# um conjunto indeterminado de temperaturas,
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

laco = True
soma = 0
qtd = 0
temperaturas = []

while laco == True:
    opcao = int(input("""
                          Você deseja:
                        1 - Informa a temperatura:
                        2 - Sair
                            """))
    
    if opcao == 1:
            temp= float(input("Informe uma temperatura: "))
            temperaturas.append(temp)
            soma = sum(temperaturas)
            qtd +=1
            
            
    if opcao == 2:
        maior = (max(temperaturas))
        menor = min(temperaturas)        
        print(f"""
          A Maior temperatura é {maior}
          A Menor temperatura é {menor}
          A Média das temperaturas é {(soma/qtd):.2f}
                """)
        laco = False

       