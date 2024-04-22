# Informe a temperatura em C em F   (0 °C × 9/5) + 32 = 32 °F

celcius = float(input('Digite uma temperatura em °C: '))
f = ((celcius * 9) / 5) + 32
print('A temperatura de {} °C corresponde a {} °F!'.format(celcius,f))
