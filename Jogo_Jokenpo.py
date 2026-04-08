from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ]PEDRA
[ 1 ]PAPEL
[ 2 ]TESOURA''')
jog = int(input('Qual é a sua jogada? '))

if jog >= len(itens):
    print('\033[2;31mJogada inválida! Tente novamente.')
    exit()

print('-=' * 15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jog]))
print('-=' * 15)
if computador == 0:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('VOCÊ VENCEU!')
    elif jog == 2:
        print('COMPUTADOR VENCEU!')
elif computador == 1:
    if jog == 0:
        print('COMPUTADOR VENCEU!')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('VOCÊ VENCEU!')
elif computador == 2:
    if jog == 0:
        print('VOCÊ VENCEU!')
    elif jog == 1:
        print('COMPUTADOR VENCEU')
    elif jog == 2:
        print('EMPATE')
