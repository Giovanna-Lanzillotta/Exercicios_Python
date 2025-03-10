# 2. Faça um programa que leia um nome de usuário e sua senha e não aceite a senha igual ao nome do usuário,
#monstrando uma mensagem de erro e voltando a pedir as informações.

laco = True

while laco:
    nome = input("Informe seu nome: ")
    senha = input("Informe sua senha: ")
    if nome != senha:
        print("Cadastro feito com sucesso! ✅")
        laco = False
    else:
        print("❌ O nome e a senha não pode ser a mesma!\n Informe novamente: ")