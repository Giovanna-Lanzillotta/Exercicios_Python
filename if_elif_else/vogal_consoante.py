#1. Faça um programa que verifique se uma letra é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print(f"{letra} é uma vogal!")
else:
    print(f"{letra} é uma consoante!")   