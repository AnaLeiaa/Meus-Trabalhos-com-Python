from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS DANADA! VOCÊ ME VENCEU!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

def flagAnaGostosa(anagostosa = True):
    if anagostosa:
        print('Ana Léia é Gostosa')
    else:
        print('Ana Léia é feia')

flagAnaGostosa(False)






