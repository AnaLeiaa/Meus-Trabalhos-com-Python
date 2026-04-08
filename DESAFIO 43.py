peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está sobrepeso ')
elif 30 <= imc < 40:
    print('Você está em Obesidade.')
else:
    print('Você está em obesidade morbida, cuidado!')
