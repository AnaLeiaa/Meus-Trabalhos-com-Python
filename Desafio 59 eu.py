from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while True:
    print('[ 1 ] Somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] outros valores\n[ 5 ] encerrar')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {} '.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('informe outro valor: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida, tente novamente! ')
    print('>=<' * 20)
    sleep(1.5)
print('Fim')



