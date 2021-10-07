# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçãoes sobre ele.

a = input('digite algo ')

print('O tipo primitivo é', type(a))
print('É alfabética?', a.isalpha())
print('É numérica?' , a.isnumeric())
print('É alfanumérica?', a.isalnum())
print('Tem espaço?', a.isspace())