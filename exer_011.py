# Faça umn programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m². 

largura = float(input("digite a largura da parede em metros "))
altura = float(input("digite a altura da parede em metros "))
area = largura * altura
tinta = area / 2

print(f'Você vai precisar de {tinta} litros de tinta')
 