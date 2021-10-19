# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escreevendo o nome escolhido.

import random

a1 = input("noem do aluno ")
a2 = input("nome do aluno ") 
a3 = input("nome do aluno ")
a4 = input("nome do aluno ")

lista = [a1,a2,a3,a4]


print(f'O aluno escolhido foi', random.choice(lista))