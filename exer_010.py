# Crie um programa que leia qunato dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

# Considere US$1.00 = R$ = 3.27 (saudades)

dinheiro = float(input("Quanto você tem na sua carteira? R$ "))

dolar = 3.27

podeComprar = dinheiro / dolar

print(f'Com {dinheiro:.2f} você é capaz de comprar {podeComprar:.2f} dólares.')