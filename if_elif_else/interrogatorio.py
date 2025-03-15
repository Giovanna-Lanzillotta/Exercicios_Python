# 21. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.As perguntas são:
# "Telefonou para vitima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou para a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa sobre oc crime.Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como "suspeita",entre 3 e 4 como "cúmplice" e 
# 5 como "assassino". Caso contrário, ele será classificado como "inocente".

pergunta1 = input("Telefonou para vitima?")
pergunta2 = input("Esteve no local do crime?")
pergunta3 = input("Mora perto da vítima?")
pergunta4 = input("Devia para vítima?")
pergunta5 = input("Já trabalho para a vítima?")

pontuacao = 0

if pergunta1 == "sim":
    pontuacao +=1
if pergunta2 == "sim":
    pontuacao +=1
if pergunta3 == "sim":
    pontuacao +=1
if pergunta4 == "sim":
    pontuacao +=1
if pergunta5 == "sim":
    pontuacao +=1

if pontuacao == 1:
    print("Inocente")
elif pontuacao == 2:
    print("Suspeita")
elif pontuacao == 3 or pontuacao == 4:
    print("cúmplice")
else:
    print("Assassino")