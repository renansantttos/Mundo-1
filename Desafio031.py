# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Qual é a distância da sua viagem? '))
viagempequena = viagem * 0.50
viagemlonga = viagem * 0.45

if viagem <= 200:
    print('Você está prestes a começar uma viagem de {}Km.'.format(viagem))
    print('E o preço da sua passagem será de R${}'.format(viagempequena))
else:
    print('Você está prestes a começar uma viagem de {}Km.'.format(viagem))
    print('E o preço da sua passagem será de R${}'.format(viagemlonga))
