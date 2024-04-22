# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o valor de um produto: '))
desconto = produto * (5 / 100)
pfinal = produto - desconto
print('O valor do produto é {} e com 5 porcento de desconto fica {}'.format(produto,pfinal))
