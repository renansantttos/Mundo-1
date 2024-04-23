#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número qualquer: '))

if n % 2 == 0:
    print('O número {} é \33[34mPAR\33[m!'.format(n))

else:
    print('o número {} é \33[35mIMPAR\33[m!'.format(n))
