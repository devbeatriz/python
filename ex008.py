# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distância em metros: '))
print('A medida de {}m correspondea {:.0f}cm e {:.0f}mm'.format(medida,medida * 100, medida * 1000))
