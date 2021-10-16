# Faça um program que leia o comprimento do lado do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

catOposto = float(input("Digite o cateto oposto "))

catAdj = float(input("Digite o cateto adjacente "))

hipotenusa = (catOposto ** 2 + catAdj ** 2) ** (1/2)

print(f'A hipotenusa dos valores digitados é {hipotenusa:.2f}')

