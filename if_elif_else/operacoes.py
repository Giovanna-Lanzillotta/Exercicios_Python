# 20.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

operacao = int(input(f"""
    Qual operação você deseja realizar:
            1 - Adição
            2 - Subtração
            3 - Multiplicação
            4 - Divisão
 
            """))

# Adição
if operacao == 1:
    op = "+"
    resultado = numero1 + numero2

# Subtração
elif operacao == 2:
    op = "-"
    resultado = numero1 - numero2

# Multiplicação
elif operacao == 3:
    op = "*"
    resultado = numero1 * numero2

# Divisão
elif operacao == 4:
    op = "/"
    resultado = numero1 / numero2

# Após o resultado

# Par ou ímpar
if resultado % 2 == 0:
    par_ou_impar = "par"
else: 
    par_ou_impar = "ímpar"

# Positivo ou Negativo
if resultado >= 0:
    positivo_ou_negativo = "positivo"
else:
    positivo_ou_negativo = "negativo"

# Inteiro ou Decimal
arredonda = round(resultado)

if resultado == arredonda:
    inteiro_ou_decimal = "inteiro"
else:
    inteiro_ou_decimal = "decimal"

print(f"""
     {numero1} {op} {numero2} = {resultado:.2f}
    O resultado = {resultado:.2f}
    É {par_ou_impar}
    , {positivo_ou_negativo}
    e {inteiro_ou_decimal}
      """)
