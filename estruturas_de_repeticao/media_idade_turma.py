# 25.Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a 
# média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

total_idade = 0
alunos = int(input("qual a quantidade de alunos: "))
for i in range(alunos):

    idade = int(input("Qual a sua idade "))
    total_idade +=idade
    media = total_idade/alunos
    
if media > 0 and media <= 25:
    print(f"Com uma média de {media:.2f} essa é uma turma jovem 😎")
elif media > 25 and media <=60:
    print(f"Com uma média de {media:.2f} essa é uma turma adulta 😁")
else :
    print(f"Com uma média de {media:.2f} essa é uma turma idosa 😊")