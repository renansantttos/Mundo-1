# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
nd = n * 2
nt = n * 3
nr = n ** (1/2)
print('O dobro de {} vale {}.'.format(n,nd))
print('O triplo de {} vale {}.'.format(n,nt))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n,nr))
