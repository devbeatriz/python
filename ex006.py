# Crie um algoritmo que leia um número e mostre os eu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(n,(n*2)))
print('O triplo de {} vale {} \nE a raiz quadrada de {} vale {:.2f}'.format(n, (n*3), n, (n**(1/2))))
