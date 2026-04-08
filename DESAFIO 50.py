s = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite o {}º valor: '.format(c)))
    if n1 % 2 == 0:
        s += n1
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, s))











