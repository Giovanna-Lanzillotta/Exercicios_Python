# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).


laco = True

while laco:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        idade = int(input("Digite sua idade: "))
        if idade >= 0  and idade <= 150:
            salario = float(input("Digite o salario: "))
            if salario >=0:
                sexo = input("Digite o sexo: ")
                if sexo == "f" or sexo =="m":
                    estado_civil = input("Digite o estado civil: ")
                    if estado_civil =="s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
                        print(f"""
                            NOME: {nome}
                            IDADE: {idade}
                            SALÁRIO: {salario}
                            SEXO: {sexo}
                            ESTADO CIVIL: {estado_civil}
                              """)
