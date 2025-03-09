#2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o
# seguinte resultado:

# A mensagem "Aprovado" se a média for maior ou igual a sete;
# A mensagem "Reprovado" se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))

media = (nota_1 + nota_2)/2

if media == 10:
    print(f"Sua média foi: {media:.2f}\n🥇 Aprovado com Distinção!")
elif media >= 7:
    print(f"Sua média foi: {media:.2f}\n📗 Aprovado!")
else:
    print(f"Sua média foi: {media:.2f}\n💣 Reprovado!")