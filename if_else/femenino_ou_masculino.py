# 3. Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input (f"""Digite
              F ou M
              :
              """)

if sexo == "F":
    print("Feminino")
else:
    if sexo == "M":
         print("Masculino")
    else:
        print("Sexo Inválido.")

