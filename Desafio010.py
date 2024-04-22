# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Quantos reais você tem na carteira? R$'))
dolar = dinheiro / 3.27
print('Você pode comprar {:.2f} em Dólar!'.format(dolar))