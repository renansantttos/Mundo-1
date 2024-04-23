# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. #aumento = sal * (15 / 100)

sal = float(input('Qual é o salário do funcionário? R$'))

if sal <= 1250:
    saln = sal + (sal * (15 / 100))
    print('Quem ganhava R${} passa a ganhar R${} agora'.format(sal,saln))
else:
    saln = sal + (sal * (10 / 100))
    print('Quem ganhava R${} passa a ganhar R${} agora'.format(sal,saln))
