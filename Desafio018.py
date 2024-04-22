# faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo.


import math
angulo = int(input('Digite o ângulo que você deseja: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('O ângulo de {} tem o SENO de {:.2f} \n O Angulo de {} tem o COSSENO de {:.2f} \n O Angulo de {} tem a TANGENTE de {:.2f}'.format(angulo,seno,angulo,cosseno,angulo,tangente))
