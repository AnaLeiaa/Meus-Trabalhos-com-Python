id = int(input('Quantos anos você tem? '))
fal = 17 - id
pas = id - 28
if id < 17:
    print('Você ainda vai se alistar para o exercito, falta {} anos.'.format(fal))
elif id <= 28:
    print('Está na hora de se alistar!')
elif id > 28:
    print('Passou do tempo de se alistar, passou {} anos'.format(pas))

