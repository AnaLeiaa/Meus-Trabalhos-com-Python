vel = float(input('Qual a velocidade do seu carro? '))
if vel > 80:
    print('Você recebeu o limite permitido que é 80km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('tenha um bom dia, dirija com segurança! ')
