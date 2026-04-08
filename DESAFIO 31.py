distancia = float(input('Qual a distancia da sua viagem? '))
print('Você está preste a começar uma velocidade de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preco))
