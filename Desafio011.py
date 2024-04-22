# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Digite a Altura da parede: '))
largura = float(input('Digite a Largura da parede: '))
area = altura * largura
tinta = 2
litros = area / tinta
print('A área da sua parede é de {}m² e a quantidade de litros de tinta são {:.2f}l de tinta.'.format(area,litros))
