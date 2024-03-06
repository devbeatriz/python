# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 4.95
euro = real / 5.39
print('Com R${:.2f} você pode comprar US{:.2f}'.format(real,dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real,euro))
