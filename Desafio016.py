# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. ex: digite um número: 6.127.   O número 6.127 tem a parte inteira 6. Dica: funçõe dentro da clase math


import math
n = float(input('Digite um número: '))
nreal = math.trunc(n)
print('O número {} tem a parte inteira {}.'.format(n,nreal))
