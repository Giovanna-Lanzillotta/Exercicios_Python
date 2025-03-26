# 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o 
# valor médio gasto em cada um deles.O usuário deverá informar a quantidade de CDs e o valor para e cada um.


quantidade_de_cds = int(input("📦 Qual a quantidade de Cds: "))
total_preco_cd = 0

for cds in range(quantidade_de_cds):
   preco_cd = float(input("💰 Qual o preco do Cd: "))
   total_preco_cd +=preco_cd
   media = total_preco_cd/quantidade_de_cds

print(f"""
     💿 COLEÇÃO DE CDs 💿
Quantidade de Cds: {quantidade_de_cds}
Média dos preços dos CDs R$: {media:.2f}
      """)