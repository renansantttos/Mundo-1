# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite o valor em metros: '))
n2 = n1 * 100
n3 = n1 * 1000
print('{} metros é: {} centimetros e {} milimetros!'.format(n1,n2,n3))
