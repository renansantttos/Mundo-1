# crie um programa que leia o nome completo de uma pessoa e mostre: 1 - o nome com todas as letras maisculas 2- o nome com todas minusculas 3- quantas letras ao todo (sem considrerar espaços) 4- quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ').strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em maiúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
