# 13. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau 
# e o programa não deve fazer pedir os demais valores, sendo encerrado;

# Se o delta calculado for negativo, a equação não possui raizes reais. 
# Informe ao usuário e encerre o programa;
#  Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# PS: digite 'import math' no início de seu script. 
# Para achar a raiz quadrada da variável x, faça: math.sqrt(x)

import math

print("Equação do Segundo grau: ax² + bx + c = y ")
a = float(input("Informe um valor para a: "))
# Não é equação do segundo grau (a =0)
if a == 0:
    print("Não é uma equação do segundo grau!")
else:   
    b = float(input("Informe um número para b: "))
    c = float(input("Informe um número para c: "))

    delta = (-b)**2 - 4 * a * c

    # Não possui raiz real
    if delta < 0:
       print("Não possui raizes reais")

    # Uma raiz real
    elif delta == 0:
     print("Uma raiz real")
     raiz = -b / (2*a)
     print(f"raiz: {raiz}")

    # Duas raizes reais
    elif delta > 0 :
       print("Duas raizes reais")
       raiz1 = (-b + math.sqrt(delta) ) / (2*a)
       raiz2 = (-b - math.sqrt(delta) ) / (2*a)
       print(f"raizes: {raiz1} e {raiz2} ")
    



