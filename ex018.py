# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor de seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cos = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
