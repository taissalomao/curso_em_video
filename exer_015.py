# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.


dias = int(input("Por quantos dias ?"))
km = float(input("Quantos kms foram rodados? "))

precoApagar = (km * 0.15) + (dias * 60)

print(f'O valor total a pagar é R$ {precoApagar:.2f}')

