# 15. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

dia = int(input("Informe um dia: "))
mes = int(input("Informe um mês: "))
ano = int(input("Informe um ano: "))

valida = False

   
# Meses com 31 dias: janeiro(1), março(3), maio(5), julho(7), agosto(8), outubro(10) e dezembro(12)
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if dia <=31: 
             print(f"""
                   Data válida
                   {dia}/{mes}/{ano}
                   """)
# Meses com 30 dias: abril(4), junho(6), setembro(9) e novembro(11)
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if dia <=30:
        print(f"""
                   Data válida
                   {dia}/{mes}/{ano}
                   """)

# Fevereiro
elif(mes == 2):
       if (ano % 4 == 0): 
          if (dia <=29):
               print(f"""
                   Data válida e ano bissexto
                   {dia}/{mes}/{ano}
                   """)
       elif(dia <=28):
              print(f"""
                   Data válida
                   {dia}/{mes}/{ano}
                   """)

elif (mes > 12):
     if dia > 32:
        print("Data inválida")

