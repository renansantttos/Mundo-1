# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valorDia = 60
kmrodado = 0.15

valorApagar = (dias * valorDia) + (km * kmrodado)
print('O total a pagar é de R$ {:.2f}'.format(valorApagar))
