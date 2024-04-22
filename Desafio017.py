# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math
cp = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hipo = math.hypot(cp,ca)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
