# 7.Faça um programa que pergunte em turno você estuda.Peça para digitar M - matutino ou V - vespertino ou N - noturno
#Imprima a mensagem "bom dia","boa tarde" ou "boa noite" ou 'valor inválido, conforme o caso.

turno = input(f"""
    QUAL TURNO VOCÊ ESTUDA
    M - MATUTINO
    V - VESPERTINO
    N - NOTURNO
     """)

if turno.lower() == "m":
    print("☀ Bom Dia!")
elif turno.lower() == "v":
    print("⛅ Boa Tarde!")
elif turno.lower() == "n":
    print("🌙 Boa Noite!")
else:
    print("❗ Valor Inválido!")