# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc
num = float(input("Digite um valor "))

print(f'O valor digitado foi {num} e a sua fração inteira é {trunc(num)}')