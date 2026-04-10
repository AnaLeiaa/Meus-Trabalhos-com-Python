print('\033[1;34m{:=^40}'.format('\033[1;34mLOJA SERAPHINA'))
preço = float(input('preço das compras: R$ '))
print('''\033[3;37mFORMA DE PAGAMENTO
[ 1 ]á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao ==1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 /100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else:
    total = 0
    print('\033[2;31mOpção invalida, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))

