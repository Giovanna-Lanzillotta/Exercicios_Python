#2. Você está no Brasil, e para temperatura usamos graus,celsius.
#Pórem, quando você for contratato para trabalhar como programador Python no exterior,deveráusar graus Fahrenheit

#A fórmula da conversão á a seguinte:
#F = 9/5 * C + 32
#Ou seja, você fornece a temperatura em graus Celsius,e seu script faz a conversão ára graus fahrenheit.

temperatura_c = float(input("Informe a temperatura em celisus "))

temperatura_f = (9/5 * temperatura_c) + 32

print(f"A temperatura de {temperatura_c:.2f} ºC fica {temperatura_f:.2f} ºF")