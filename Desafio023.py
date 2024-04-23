# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Informe um número: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print('Analisando o número {}'.format(n))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
