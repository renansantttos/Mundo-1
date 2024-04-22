# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sal = float(input('Digite o seu salário: '))
aumento = sal * (15 / 100)
novosal = sal + aumento
print('O seu salário de {} reais com o aumento de 15 porcento fica em {:.2f} reais!'.format(sal,novosal))
