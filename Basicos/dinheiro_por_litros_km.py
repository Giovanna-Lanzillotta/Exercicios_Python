# 04. Um novo modelo de carro, super econômico foi lançado.
# Ele faz 20 km com 1 litro de combustível.
# Cada litro de combustível custa R$ 5,00

# Faça um programa que pergunte ao usuário quanto dinheiro ele tem e em seguida diga quantos litros de 
#combustível ele pode comprar e quantos kilometros o carro consegue andar com este tanto de combustível.
#Seu script será usado no computador de bordo do carro.

dinheiro = float(input("Quanto de dinheiro você tem?"))

litros_combustivel = dinheiro / 5
kilometros = litros_combustivel * 20

print(f"""
===============================
💰 Você tem R$ {dinheiro:.2f}
⛽ Com isso compra {litros_combustivel:.2f} litros
🚗 e consegue andar {kilometros:.2f} KM
===============================
      """)