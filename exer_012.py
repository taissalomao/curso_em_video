# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

precoProduto = float(input("Digite o valor do produto "))

desconto = (precoProduto * 5 )/ 100

precoFinal = precoProduto - desconto

print(f'O valor do produto com desconto é de {precoFinal:.2f}')

