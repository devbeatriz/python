# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# Para salários supeiores a R$1.250,00, calcule um aumento de 10%
# Para os inferioes ou iguais, o aumento e de 15%
salario = float(input('Qual o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,novo))
