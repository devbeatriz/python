# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# faça um programa que ajude ele, sorteando o nome de um dos alunos.
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print('O aluno sorteado foi: {}'.format(sorteado))
