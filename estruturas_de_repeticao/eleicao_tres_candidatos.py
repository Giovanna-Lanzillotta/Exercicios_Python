# 26. Numa eleição existem três candidatos.Faça um programa que peça o número total de eleitores.Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato.

canditadoA = 0
canditadoB = 0
canditadoC = 0

total_eleitores = int(input("Qual o número total de eleitores: "))
for eleitor in range(total_eleitores):
   voto = int(input(f""" Digite o número do seu candidato:
                    1 - Candidato A 🐶
                    2 - Candidato B 😸
                    3 - Candidato C 🐸
                    """))
   if voto == 1:
      canditadoA +=1 

   elif voto == 2:
      canditadoB +=1

   elif voto == 3:
      canditadoC +=1
    
if canditadoA > canditadoB and canditadoA > canditadoB:
 vencedor = "canditado A 🐶"

     
if canditadoB > canditadoA and canditadoB > canditadoC:
 vencedor = "canditado B 😺"

     
if canditadoC > canditadoA and canditadoC > canditadoB:
 vencedor = "canditado C 🐸"

print(f"""
🗳 Total de eleitores: {total_eleitores}
🐶 Votos do candidato A: {canditadoA}
😺 Votos do candidato B: {canditadoB}
🐸 Votos do candidato C: {canditadoC}
VENCEDOR: {vencedor}
      """)

 