from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em número entre 0 e 10.')
print('Será que você consegue acertar?')

palpites = 0
while True:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        break
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        else:
            print('Menos... tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))





